import boto3
import json

aws_ec2 = boto3.client('ec2')
response = aws_ec2.describe_instances()

print(response)
