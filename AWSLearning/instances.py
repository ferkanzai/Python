import boto3, json, re, time, os, base64, rsa
from tabulate import tabulate

ec2 = boto3.client('ec2')

region_regex = '[a-z]{2}-[a-z]{4,7}-[0-9]{1}'
list_regions = [[ec2.describe_regions()["Regions"][i]["RegionName"]] for i in range(len(ec2.describe_regions()["Regions"]))]
pem_file_loc = os.path.expanduser('~/windows.pem')


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
    region = input("What region do you want to check? (press ENTER for default region: eu-west-1)\nIf you don't know the regions, type list.\n")
    regions = []
    for test in list_regions:
        for name in test:
            regions.append(name)
    if region == "":
        region = 'eu-west-1'
        print("You are using {} region".format(region))
        break
    elif region == 'list':
        print("")
        print(tabulate(list_regions, headers=['Region'], tablefmt='github'), "\n")
    elif region in regions:
        print("You are using {} region".format(region))
        break
    else:
        print("Not a valid region\n")

ec2 = boto3.client('ec2', region_name=region)

while True:
    
    print("")
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
            print("\nThere are no running instances")
        else:
            instance_list = []
            for reservation in response['Reservations']:
                instances = reservation['Instances']
                for instance in instances:
                    i_id = instance['InstanceId']
                    tags = instance['Tags']
                    for tag in tags:
                        if tag['Key'] == 'Name':
                            name = tag['Value']
                    instance_list.append([name, i_id])
            print("")
            print(tabulate(instance_list, headers=['Instance name', 'Instance ID'], tablefmt='github'))

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
            print("\nThere are no stopped instances")
        else:
            instance_list = []
            for reservation in response['Reservations']:
                instances = reservation['Instances']
                for instance in instances:
                    i_id = instance['InstanceId']
                    tags = instance['Tags']
                    for tag in tags:
                        if tag['Key'] == 'Name':
                            name = tag['Value']
                    instance_list.append([name, i_id])
            print("")
            print(tabulate(instance_list, headers=['Instance name', 'Instance ID'], tablefmt='github'))

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
        print("Instance {} is STARTED".format(i_id))

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
        print("Instance {} is STOPPED".format(i_id))

    elif choice == '5':
        public_ip = ''
        i_id = input("\nInstance ID you want SSH to:\n")
        response = ec2.describe_instances(
            InstanceIds=[
                i_id
            ]
        )
        public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
        print("")
        os.system("ssh -i ~/linux.pem ec2-user@{} -o \"StrictHostKeyChecking no\"".format(public_ip))
    elif choice == '6':
        i_id = input("\nWindows Instance ID from which you want to decrypt the password:\n")
        response = ec2.get_password_data(
            InstanceId=i_id
        )
        pswd_encrypted = base64.b64decode(response['PasswordData'])
        if pswd_encrypted:
            with open (pem_file_loc,'r') as privkeyfile:
                priv = rsa.PrivateKey.load_pkcs1(privkeyfile.read())
            key = rsa.decrypt(pswd_encrypted,priv)
        else:
            key = 'Wait at least 4 minutes after creation before the admin password is available'
        print("\nThe password is: {}".format(key))
    elif choice == '7':
        break
    else:
        print('Invalid option, please, enter a valid number:\n')