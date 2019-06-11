#this file gets a file uploaded to S3, downloads it, zipps it and uploads it back to S3

import json
import boto3
import os
from zipfile import ZipFile

s3 = boto3.client('s3')

def lambda_handler(event, context):

    #print(json.dumps(event))

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    name = key.split('.')[0]
    #print(name)

    download_path = '/tmp/{}.jpg'.format(name)
    #print(download_path)

    upload_path = '/tmp/{}.zip'.format(name)
    #print(upload_path)

    upload_key = '{}.zip'.format(name)

    s3.download_file(bucket, key, download_path)

    with ZipFile('/tmp/{}.zip'.format(name),'w') as zip:
        zip.write(download_path)

    s3.upload_file(upload_path, bucket, upload_key)
