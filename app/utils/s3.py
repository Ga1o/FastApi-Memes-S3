import boto3
import os
import aiofiles
from botocore.client import Config


MINIO_URL = os.getenv('MINIO_URL', 'http://localhost:9000')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY')
MINIO_BUCKET = os.getenv('MINIO_BUCKET')

s3_client = boto3.client(
    's3',
    endpoint_url=MINIO_URL,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY,
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)


async def upload_file(file, file_name):
    async with aiofiles.open(file, 'rb') as f:
        s3_client.upload_fileobj(f, MINIO_BUCKET, file_name)
    return f'{MINIO_URL}/{MINIO_BUCKET}/{file_name}'
