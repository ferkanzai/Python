import boto3
import json
#from datetime import date, datetime

boto3.setup_default_session(region_name='eu-west-1')
ec2 = boto3.client('ec2')
#response = ec2.describe_instances()

paginator = ec2.get_paginator('describe_instances')
instances = paginator.paginate().build_full_result()

instance_list = []
try:
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_list.append(instance['InstanceId'])

        #for i in image['Images']:
        #    client.modify_instance_attribute(InstanceId=image, Groups=['Default',])

print(instance_list)

#for i in response:
#    print(i['Reservations'][i]['Instances'][i]['InstanceId'])
#print(response)
#print(json.dumps(response, indent=4, sort_keys=True, default=str))
