import boto3, json
#from tabulate import tabulate

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

#regions = ec2.describe_regions()["Regions"]
list_regions = [ec2.describe_regions()["Regions"][i]["RegionName"] for i in range(len(ec2.describe_regions()["Regions"]))]
#print(tabulate(list_regions, headers=['Region Name'], tablefmt='github'))
for region in list_regions:
    print(region)