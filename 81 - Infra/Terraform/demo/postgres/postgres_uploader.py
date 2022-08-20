# Databricks notebook source
pip install sqlalchemy

# COMMAND ----------

import sqlalchemy as db
from utils import get_token, upload_to_postgress
import pandas as pd
# Database
port = get_token("dash_postgres_secret", "ee_port")
host = get_token("dash_postgres_secret", "ee_host")
user = get_token("dash_postgres_secret", "username")
pwd = get_token("dash_postgres_secret", "password")
env = 'dev'
engine = db.create_engine(f"postgresql://{user}:{pwd}@{host}:{port}/{env}")
df = spark.table("employee_engagement.glassdoor").toPandas()
df.sort_values('record_create_dt', ascending=False, inplace=True)
df.drop_duplicates('external_id', keep='first', inplace=True)
cols = ['external_id', 'business_name', 'review_url', 'review_title']
df['review_url'] = df['site'] + df['review_url']
drop_cols = ['record_create_dt', 'site', 'context_identifier', 'execution_id', 'record_create_by', 
             'file_create_dt', 'city', 'state']
df.drop(columns=drop_cols)
df.rename(columns={'business_name' : 'brand'}, inplace=True)
df = df.astype({
    "external_id": int,
    "review_date": 'datetime64[ns]',
    "overall_rating" : float,
    "culture_and_values" : float,
    "work_life_balance" : float,
    "senior_management" : float,
    "compensation_and_benefits" : float,
    "career_opportunities" : float,
    "years_at_company" : int,
  
})

upload_to_postgress({
        "main_db" : df,
      }, con=engine)

# COMMAND ----------

### QC ###
query = '''
SELECT brand, review_date, AVG(overall_rating) as mean_rating FROM main_db
WHERE brand = 'Amazon'
AND review_date >= '2021-01-01'
GROUP BY brand, review_date
'''
d1 = pd.read_sql(query, con=engine)
d1

# COMMAND ----------


