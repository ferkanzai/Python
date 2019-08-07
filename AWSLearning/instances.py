import boto3, json, re

region_regex = '[a-z]{2}-[a-z]{4,7}-[0-9]{1}'

def check(region):
    if re.search(region_regex, region):
        return True

while True:
    region = input("What region do you want to check? (eu-west-1 is default)\n")
    if region == "":
        region = 'eu-west-1'
        print("You are using {} region\n".format(region))
        break
    else:
        if check(region):
            print("\nYou are using {} region\n".format(region))
            break
        else:
            print("\nNot a valid region\n")

ec2 = boto3.client('ec2', region_name=region)

while True:
    
    print("Check EC2 instances:")
    print("Choose an option:")
    print("1. Running instances")
    print("2. Stopped instances")
    print("3. Start instance (press ENTER to exit)")
    print("4. Stop instance (press ENTER to exit)")
    print("5. SSH to instance (press ENTER to exit)")
    print("6. Decrypt password for Windows instances (press ENTER to exit)")
    print("7. Exit")
    print("")
    choice = input("Enter your choice number:\n")

    if choice =='1':
        response = ec2.describe_instances(Filters=[
                {
                    'Name': 'instance-state-code',
                    'Values': [
                        '16'
                    ]
                }
            ]
        )
        if len(response['Reservations']) == 0:
            print("\nThere are no running instances\n")
        else:
            instance_list = []
            #instances = response['Reservations'][0]['Instances']
            for reservation in response['Reservations']:
                instances = reservation['Instances']
                for instance in instances:
                    i_id = instance['InstanceId']
                    tags = instance['Tags']
                    for tag in tags:
                        if tag['Key'] == 'Name':
                            name = tag['Value']
                    instance_list.append({'Name': name, 'Instance ID': i_id})
            print("")
            print(json.dumps(instance_list, indent=2), "\n")

    elif choice == '2':
        response = ec2.describe_instances(Filters=[
                {
                    'Name': 'instance-state-code',
                    'Values': [
                        '80'
                    ]
                }
            ]
        )
        if len(response['Reservations']) == 0:
            print("\nThere are no stopped instances\n")
        else:
            instance_list = []
            #instances = response['Reservations'][0]['Instances']
            for reservation in response['Reservations']:
                instances = reservation['Instances']
                for instance in instances:
                    i_id = instance['InstanceId']
                    tags = instance['Tags']
                    for tag in tags:
                        if tag['Key'] == 'Name':
                            name = tag['Value']
                    instance_list.append({'Name': name, 'Instance ID': i_id})
            print("")
            print(json.dumps(instance_list, indent=2), "\n")

    elif choice == '3':
        continue
    elif choice == '4':
        continue
    elif choice == '5':
        continue
    elif choice == '6':
        continue
    elif choice == '7':
        break
    else:
        print('Invalid option, please, enter a valid number:\n')