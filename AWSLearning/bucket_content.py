import json
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

buckets = [s3.list_buckets()["Buckets"][i]["Name"] for i in range(len(s3.list_buckets()["Buckets"]))]
#print(buckets)
#print(s3.list_objects_v2(Bucket=buckets[0]))

for bucket in buckets:

    try:
        contents = s3.list_objects_v2(Bucket=bucket)['Contents']
    except KeyError:
        print("Bucket {} is empty \n".format(bucket))
        continue
    
    contents = s3.list_objects_v2(Bucket=bucket)["Contents"]
    keys = [contents[i]["Key"] for i in range(len(contents))]

    if len(keys) <= 5:
        print("Bucket {} has the following objects:".format(bucket))
        string = ""
        for key in keys:
            string += string + key + "\n"
        print(string)
    else:
        print("Bucket {} has too many objects \n".format(bucket))