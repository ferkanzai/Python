import boto3
import json

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

regions = ec2.describe_regions()["Regions"]
list_regions = []

for i in range(len(regions)):
    list_regions.append(regions[i]["RegionName"])

    