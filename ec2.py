import boto3
import json

while True:

    print('====EC2 instances helper====')
    print('')
    print('1. Running instances in a region')
    print('2. Stopped instances in a region')
    print('3. Start instance')
    print('4. Stop instance')
    print('5. All instances in all regions')
    print('6. Exit')
    print('')
    option = input('Choose an option: ')
    print('')

    if (option == '1'):
        client = boto3.client('ec2')
        regions = client.describe_regions()
        region = input('Choose a region: ')
        if (region in regions):
            ec2 = boto3.client('ec2', region_name=region)
        else:
            print('Not a region')
            print('')

    elif (option == '5'):

        ec2 = boto3.client('ec2')

        regions = ec2.describe_regions()
        for region in regions["Regions"]:
            region = region["RegionName"]

            listInst = []
            listName = []
            client = boto3.client('ec2', region_name=region)
            instances = client.describe_instances()
            for reservation in instances["Reservations"]:
                for instance in reservation["Instances"]:
                    listInst.append(instance["InstanceId"])
                    for name in instance["Tags"]:
                        if (name["Key"] == 'Name'):
                            listName.append(name["Value"])

            if (not listInst):
                print('No instances in region', region)
            else:
                print('Instances in region', region, ':')
                for i, n in zip(listInst, listName):
                    print('{} {}'.format(i, n))
        print('')
    elif (option == '6'):
        break
