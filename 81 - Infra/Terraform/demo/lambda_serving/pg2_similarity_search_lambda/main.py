import json
import utils
import pandas as pd

def handler(event, context):
    if "body" in event:
        # For API Gateway
        event = json.loads(event["body"])

    query_text = event["query_text"]
    count =  event.get("k", 10)
    score_threshold = event.get("score_threshold", 0)
    brand = event.get("brand", "All")

    ### compute embedding
    query_embeddings = utils.compute_embeddings(query_text)

    ### Find top K chunks from opensearch
    df_sim = utils.find_top_k_chunks(
        index_name="employee_engagement_index", 
        k=count, 
        cols_to_query=["brand", "review_url", "review_date", "review_title", "overall_rating", "pros", "cons"] ,
        brand=brand, 
        embeddings=query_embeddings,
        score_threshold=score_threshold)

    df_sim['_score'] = df_sim['_score'].round(3)
    similarity_returns = {
            "query_chunk": query_text,
            "similar_text": df_sim.to_json(),
            }
    
    # For API Gateway
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(similarity_returns),
    }

### test
# event = {
#   "query_text": """working culture""",
#   "k": 5,
#   "brand": "Amazon"
# }