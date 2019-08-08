import boto3, json, os, base64, rsa

ec2 = boto3.client('ec2')

i_id = 'i-09cf2b0b75c7c5948'
pem_file_loc = os.path.expanduser('~/windows.pem')

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
 
print(key)