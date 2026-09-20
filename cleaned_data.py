import json
import pandas as pd
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Step 1: Read raw file (from local - next week we will read directly from S3)
with open("users_raw.json", "r") as f:
    data = json.load(f)

# Step 2: Flatten to DataFrame
df = pd.json_normalize(data)
print("Raw columns:", df.columns.tolist())

# Step 3: Keep only useful columns for business
# Example raw has: id, name, email, address.city, phone
clean_df = df[["id", "name", "email", "address.city", "phone"]].copy()

# Rename for Snowflake-friendly names (no dot)
clean_df.rename(columns={"address.city": "city"}, inplace=True)

print(clean_df.head(3))
print(f"Total rows: {len(clean_df)}")

# Step 4: Save as clean CSV locally
clean_df.to_csv("users_clean.csv", index=False)
print("Saved users_clean.csv")

# Step 5: Upload clean to S3
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)
bucket = os.getenv("AWS_BUCKET_NAME")
s3.upload_file("users_clean.csv", bucket, "clean/users_clean.csv")
print(f"Uploaded to s3://{bucket}/clean/users_clean.csv")