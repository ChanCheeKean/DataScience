import json
import pandas as pd
from sql import group_rating_sql, year_band_sql
from plot import create_line_rating, create_pie_rating
from constants import engine

def handler(event, context):
    if "body" in event:
        # For API Gateway
        event = json.loads(event["body"])

    query_params = {
        "start_date" :  event["start_date"],
        "end_date": event["end_date"],
        "brand": event["brand"],
    }

    ### create line rating chart
    df_rating = pd.read_sql(group_rating_sql.format(**query_params), con=engine)
    df_rating = df_rating.groupby('review_date').mean().stack().reset_index()
    df_rating.columns = ['date', 'category', 'value']
    line_fig = create_line_rating(df_rating)

    ### create pie rating 
    df_band = pd.read_sql(year_band_sql.format(**query_params), con=engine)
    pie_fig = create_pie_rating(df_band)

    ### combine result
    pg1_returns = {
        "pg1_line_rating" : line_fig.to_json(),
        "pg1_pie_rating" : pie_fig.to_json(),
        }

    # For API Gateway
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(pg1_returns),
    }

### test
# import sys
# sys.path.append("../utils")
# event = {
#   "start_date": "2021-01-01",
#   "end_date": "2021-12-31",
#   "brand": "Amazon"
# }