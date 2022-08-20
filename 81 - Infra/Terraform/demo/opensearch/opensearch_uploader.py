# Databricks notebook source
!pip install opensearch-py boto3 tqdm polling2 sentence_transformers

# COMMAND ----------

import pandas as pd
import numpy as np
from tqdm import tqdm
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
from opensearchpy.helpers import bulk
import boto3
import requests
import polling2
import logging
from random import randint
import plotly.express as px
from sklearn.metrics.pairwise import euclidean_distances
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L12-v2')

# COMMAND ----------

articles = spark.table('employee_engagement.glassdoor_review_embedding').toPandas()
articles['review_date'] = pd.to_datetime(articles['review_date'])
articles['record_create_dt'] = pd.to_datetime(articles['record_create_dt'])

# 99% the duplicate_id has identical content
print(articles[articles.duplicated(['external_id'], keep=False)].shape)
print(articles[articles.duplicated(['external_id', 'review_text'], keep=False)].shape)
print(articles[articles.duplicated(['external_id', 'pros'], keep=False)].shape)
print(articles[articles.duplicated(['external_id', 'cons'], keep=False)].shape)

# drop duplicates and pick up the latest review
articles.sort_values('record_create_dt', ascending=False, inplace=True)
articles.drop_duplicates('external_id', keep='first', inplace=True)
articles = articles.rename(columns={'external_id': 'id', 'business_name' : 'brand'})
articles.drop(columns=['record_create_dt', 'review_text', 'company_id'], inplace=True)
print(articles.shape)

# COMMAND ----------

### connecting to opensearch api
host = "search-mynewdomain-gp74byna6ivfgazl4upbhbclfe.us-east-1.es.amazonaws.com"
port = 443
region = 'us-east-1'
credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region)

client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

### helper function
def upload_data(client, index_name, df, chunk_size=500):
    for idx in tqdm(range(0, len(df), chunk_size)):
        # Upload chunk_size number of rows at a time
        subset_df = df.iloc[idx:idx + chunk_size]
        actions = [
            {
                '_index': index_name,
                '_id': row.id,
                '_source': {
                    key: value 
                    for key, value in row._asdict().items() 
                    if key not in ['Index', 'id']
                }
            } for row in subset_df.itertuples()
        ]

        _, errors = bulk(client, actions, max_retries=2, request_timeout=100)
        assert len(errors) == 0, errors

    # Refresh the data
    client.indices.refresh(index_name, request_timeout=1000)
    
# def find_top_k_chunks(
#     embeddings,
#     k,
#     cols_to_query,
#     index_name,
#     client,
#     emb_col,
#     chunk_size=500,
# ):

#     req_head = {"index": index_name}
#     responses = []

#     for idx in range(0, len(embeddings), chunk_size):
#         subset_embeddings = embeddings[idx : idx + chunk_size]
#         request = []

#         for embedding in subset_embeddings:
#             req_body = {
#                 "query": {"knn": {emb_col: {"vector": embedding, "k": k}}},
#                 "size": k,
#                 "_source": cols_to_query,
#             }

#             request.extend([req_head, req_body])

#         r = client.msearch(body=request)
#         responses.extend(r["responses"])

#     # Post processing
#     chunks = []
#     for item in responses:
#         df = pd.DataFrame(item["hits"]["hits"])
#         df = df[["_id", "_score"]].join(pd.json_normalize(df["_source"]))
#         chunks.append(df.to_dict(orient="records"))

#     return chunks

def find_top_k_chunks(client, index_name, query, k, cols_to_query, score_threshold=0):
    req_head = {"index": index_name}
    responses = []
    req_body = {
        "query": query,
        "size": k,
        "_source": cols_to_query,
        "min_score": score_threshold
    }
    
    r = client.msearch(body=[req_head, req_body])
    df = pd.DataFrame(r["responses"][0]["hits"]["hits"])
    df = df[["_id", "_score"]].join(pd.json_normalize(df["_source"]))
    return df

### print status
url = f'https://{host}:{port}/_cat/nodes?v'
response = requests.get(url, auth=auth)
print(response.text)

url = f'https://{host}:{port}/_cat/indices?v'
response = requests.get(url, auth=auth)
print(response.text)

# COMMAND ----------

### create ANN index and upload data to opensearch
index_name = 'employee_engagement_index'
emb_col = ['review_text_embedding', 'pros_embedding', 'cons_embedding']

properties = {emb_col: {
    "type": "knn_vector",
    "dimension": len(articles.loc[0, emb_col]),
    "method": {
        "name": "hnsw", 
        "space_type": "l2", 
        "engine": "nmslib",
        "parameters": {"ef_construction": 128, "m": 24}}
} for emb_col in emb_col}

index_body = {
    'settings': {
        'index': {
            'knn': True,
            'number_of_shards': 10,
            'number_of_replicas': 0,
            'refresh_interval': -1,
        }
    },
    'mappings': {
        'properties': properties
    }
}

if client.indices.exists(index=index_name):
    # Delete the index if it exists
    client.indices.delete(index=index_name)
    
response = client.indices.create(index_name, body=index_body)
print(response)
upload_data(client, index_name=index_name, df=articles, chunk_size=500)

# COMMAND ----------

text = 'working culture'
brand = 'Amazon'
embedding = model.encode(text)
index_name = 'employee_engagement_index'
cols_to_query = ['review_title', 'brand', 'pros', 'cons'] 
k = 10

# query = {"knn": {emb_col: {"vector": embedding, "k": k}}}
query = {
        "bool": {
            "filter": [{"match": {"brand": brand},}],
            "should": [
                {"function_score": {"query": {"knn": {"review_text_embedding": {"vector": embedding, "k": k}}}, "weight": 0.2}},
                {"function_score": {"query": {"knn": {"cons_embedding": {"vector": embedding, "k": k}}}, "weight": 0.4}},
                {"function_score": {"query": {"knn": {"pros_embedding": {"vector": embedding, "k": k}}}, "weight": 0.4}},
            ]
        }
}

find_top_k_chunks(client, index_name, query, k, cols_to_query, score_threshold=.5)
