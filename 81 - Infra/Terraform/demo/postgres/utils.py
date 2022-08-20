import json
import boto3

session = boto3.session.Session()
client = session.client(service_name='secretsmanager', region_name='us-east-1')

def get_token(secret_name: str, key_name: str) -> str:
    token = json.loads(
        client.get_secret_value(
            SecretId=secret_name)['SecretString'])[key_name]
    return token

def upload_to_postgress(file_dict, con):
    print('Uploading to Postgress')
    for file_name, data in file_dict.items():
        data.to_sql(file_name, con=con, if_exists="replace") 
        print("Uploaded ", file_name)