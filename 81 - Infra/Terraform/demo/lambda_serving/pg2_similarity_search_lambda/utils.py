import re
from sentence_transformers import SentenceTransformer
import pandas as pd
import opensearch
import json
import boto3

# from sentence_transformers import SentenceTransformer
# model = SentenceTransformer('all-MiniLM-L12-v2')
# model.save('./models/all-MiniLM-L12-v2')

model = SentenceTransformer("./models/all-MiniLM-L12-v2")

def compute_embeddings(query_chunks):
    return model.encode(query_chunks).tolist()

def find_top_k_chunks(index_name, k, cols_to_query, brand, embeddings, score_threshold=0):
    client=opensearch.client
    req_head = {"index": index_name}

    # query = {"knn": {emb_col: {"vector": embedding, "k": k}}}
    query = {
        "bool": {
            "filter": [{"match": {"brand": brand},}],
            "should": [
                
                # weightage for cons embeddin
                {"function_score": {
                    "query": {"knn": {"cons_embedding": {"vector": embeddings, "k": k}}}, 
                    "functions": [
                        {"filter": {"match": {"overall_rating": 1.0}}, "weight": 1}, 
                        {"filter": {"match": {"overall_rating": 2.0}}, "weight": 0.75},
                        {"filter": {"match": {"overall_rating": 3.0}}, "weight": 0.5},
                        {"filter": {"match": {"overall_rating": 4.0}}, "weight": 0.25},
                        {"filter": {"match": {"overall_rating": 5.0}}, "weight": 0},
                        
                    ],
                }},
                
                # weightage for pros embeddin
                {"function_score": {
                    "query": {"knn": {"pros_embedding": {"vector": embeddings, "k": k}}}, 
                    "functions": [
                        {"filter": {"match": {"overall_rating": 1.0}}, "weight": 0}, 
                        {"filter": {"match": {"overall_rating": 2.0}}, "weight": 0.25},
                        {"filter": {"match": {"overall_rating": 3.0}}, "weight": 0.5},
                        {"filter": {"match": {"overall_rating": 4.0}}, "weight": 0.75},
                        {"filter": {"match": {"overall_rating": 5.0}}, "weight": 1},
                    ],
                }},
                # {"function_score": {"query": {"knn": {"review_text_embedding": {"vector": embedding, "k": k}}}, "weight": 0.4}},
            ]
        }
}

    # query = {
    #     "bool": {
    #         "filter": [{"match": {"brand": brand},}],
    #         "should": [

    #             {"function_score": {
    #                 "query": {"knn": {"review_text_embedding": {"vector": embeddings, "k": k}}}, 
    #                 "weight": 0.2}
    #                 },

    #             {"function_score": {
    #                 "query": {"knn": {"cons_embedding": {"vector": embeddings, "k": k}}}, 
    #                 "weight": 0.4}
    #                 },
                    
    #             {"function_score": {
    #                 "query": {"knn": {"pros_embedding": {"vector": embeddings, "k": k}}}, 
    #                 "weight": 0.4}
    #                 },
    #         ]
    #     }
    # }

    if brand == 'All':
        query['bool']['filter'] = []

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

# def find_top_k_chunks(
#     embeddings,
#     k,
#     score_threshold,
#     cols_to_query,
#     index_name,
#     client=opensearch.client,
#     emb_col="embedding",
#     chunk_size=500):

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
#                 "min_score": score_threshold
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