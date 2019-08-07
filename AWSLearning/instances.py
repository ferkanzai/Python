import boto3, json, re, time
from tabulate import tabulate

region_regex = '[a-z]{2}-[a-z]{4,7}-[0-9]{1}'

def check(region):
    if re.search(region_regex, region):
        return True

def check_status(i_id):
    describe_instance = ec2.describe_instances(
            InstanceIds=[
                i_id
            ]
        )
    status = describe_instance['Reservations'][0]['Instances'][0]['State']['Code']
    return status

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
    print("3. Start instance")
    print("4. Stop instance")
    print("5. SSH to instance")
    print("6. Decrypt password for Windows instances")
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
                    #instance_list.append({'Name': name, 'Instance ID': i_id})
                    instance_list.append([name, i_id])
            print("")
            #print(json.dumps(instance_list, indent=2), "\n")
            print(tabulate(instance_list, headers=['Instance name', 'Instance ID'], tablefmt='github'), "\n")

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
                    #instance_list.append({'Name': name, 'Instance ID': i_id})
                    instance_list.append([name, i_id])
            print("")
            #print(json.dumps(instance_list, indent=2), "\n")
            print(tabulate(instance_list, headers=['Instance name', 'Instance ID'], tablefmt='github'), "\n")

    elif choice == '3':
        i_id = input("\nWhich instance do you want to start?\n")
        ec2.start_instances(
            InstanceIds=[
                i_id
            ]
        )
        status = check_status(i_id)
        while status != 16:
            time.sleep(5)
            print("Instance {} still starting".format(i_id))
            status = check_status(i_id)
        print("Instance {} is STARTED\n".format(i_id))

    elif choice == '4':
        i_id = input("\nWhich instance do you want to stop?\n")
        ec2.stop_instances(
            InstanceIds=[
                i_id
            ]
        )
        status = check_status(i_id)
        while status != 80:
            time.sleep(5)
            print("Instance {} still stopping".format(i_id))
            status = check_status(i_id)
        print("Instance {} is STOPPED\n".format(i_id))

    elif choice == '5':
        continue
    elif choice == '6':
        i_id = input("\nWindows Instance ID from which you want to decrypt the password:\n")
        response = ec2.get_password_data(
            InstanceId=i_id
        )
        pswd_encrypted = response['PasswordData']
        print("\n", pswd_encrypted, "\n")
    # check https://github.com/tomrittervg/decrypt-windows-ec2-passwd/blob/master/decrypt-windows-ec2-passwd.py
    # and https://gist.github.com/tinkerbotfoo/337df5bd1faff777fb52
    elif choice == '7':
        break
    else:
        print('Invalid option, please, enter a valid number:\n')