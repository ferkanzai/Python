import boto3
import json
import os
import time

boto3.setup_default_session(region_name='eu-west-1')
ec2 = boto3.client('ec2')

paginator = ec2.get_paginator('describe_instances')
instances = paginator.paginate().build_full_result()

public_ip = ''
for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            ins_id = instance['InstanceId']
            tags = instance['Tags']
            for tag in tags:
                if tag['Key'] == 'Name' and tag['Value'] == 'RDS' and instance['State']['Name'] == 'running':
                    public_ip = instance['PublicIpAddress']
                elif tag['Key'] == 'Name' and tag['Value'] == 'RDS' and instance['State']['Name'] != 'running':
                    ec2.start_instances(InstanceIds=[ins_id])
                    ins_id.wait_until_running()

os.system("ssh -i ~/linux.pem ec2-user@{}".format(public_ip))