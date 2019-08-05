import json, re, boto3, urllib.request

s3 = boto3.client('s3')
bucket_name = 'fcadevplan'

def get_policy():
    response = s3.get_bucket_policy(Bucket=bucket_name)
    policy = json.dumps(response["Policy"])
    return policy

def get_ip():
    policy = get_policy()
    ip_policy = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', policy)
    return ip_policy[0]

def change_ip(ip):
	policy = get_policy()
	replaced = json.loads(re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip, policy))
	new_policy = s3.put_bucket_policy(
        Bucket=bucket_name,
        Policy=replaced
    )
	return new_policy

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
ip_bucket = get_ip()

print("IP on S3 is:", ip_bucket)
print("IP on my laptop is:", external_ip)

if ip_bucket == external_ip:
    print("Your actual IP is already configured in your bucket policy")
else:
    print("Changing {} for {}".format(ip_bucket, external_ip))
    change_ip(external_ip)
    print("IP on the policy was changed to {}".format(external_ip))

#print(get_policy())