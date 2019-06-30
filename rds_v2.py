import boto3,socket,time,os
from botocore.exceptions import ClientError

retries = 10
retry_delay=10
retry_count = 0

ec2 = boto3.resource('ec2',region_name="eu-west-1")
ec2_id = 'i-08ab0f4dc20a000b3'
instance = ec2.Instance(id=ec2_id)

if instance.state['Code'] == 80:
    print("starting instance {} \n".format(ec2_id))
    instance.start()
    instance.wait_until_running()

    while retry_count <= retries:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((instance.public_ip_address,22))
        try:
            if result == 0:
                print("Instance is UP & accessible on port 22, the IP address is: {} \n".format(instance.public_ip_address))
                break
            else:
                print("instance is still down retrying...")
                time.sleep(retry_delay)
        except ClientError as e:
            print('Error', e)
    os.system("ssh -i ~/linux.pem ec2-user@{} -o \"StrictHostKeyChecking no\"".format(instance.public_ip_address))
elif instance.state['Code'] == 16:
    print("Instance {} is running, connecting on port 22\n".format(ec2_id))
    os.system("ssh -i ~/linux.pem ec2-user@{} -o \"StrictHostKeyChecking no\"".format(instance.public_ip_address))
else:
    print("Instance state neither stopped nor running")