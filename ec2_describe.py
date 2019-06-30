import boto3
import json
import os
#from datetime import date, datetime

boto3.setup_default_session(region_name='eu-west-1')
ec2 = boto3.client('ec2')
#response = ec2.describe_instances()

paginator = ec2.get_paginator('describe_instances')
instances = paginator.paginate().build_full_result()

instance_list = []
instance_dict = {}
try:
    #print(paginator)
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            temp_dict = {}
            tags = instance['Tags']
            for tag in tags:
                if tag['Key'] == 'Name':
                    temp_dict['Name'] = tag['Value']
            temp_dict['Instance ID'] = instance['InstanceId']
            if instance['State']['Name'] == 'running':
                temp_dict['Public IP'] = instance['PublicIpAddress']
            instance_list.append(temp_dict)

        #for i in image['Images']:
        #    client.modify_instance_attribute(InstanceId=image, Groups=['Default',])
except:
    print('error')
instance_dict.update({'Instances': instance_list})
#print(json.dumps(instance_dict, indent=4))

#for i in response:
#    print(i['Reservations'][i]['Instances'][i]['InstanceId'])
#print(response)
#print(json.dumps(response, indent=4, sort_keys=True, default=str))
public_ip = ''
for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            tags = instance['Tags']
            for tag in tags:
                if tag['Key'] == 'Name' and tag['Value'] == 'RDS' and instance['State']['Name'] == 'running':
                    public_ip = instance['PublicIpAddress']

os.system("ssh -i ~/linux.pem ec2-user@{}".format(public_ip))