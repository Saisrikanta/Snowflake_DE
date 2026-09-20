import boto3
import os
from dotenv import load_dotenv

load_dotenv()  # loads from .env file

bucket_name = os.getenv("AWS_BUCKET_NAME")
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

s3.upload_file("users_raw.json", bucket_name, "raw/users_raw.json")
print(f"Uploaded to s3://{bucket_name}/raw/users_raw.json")