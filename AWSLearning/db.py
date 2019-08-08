import os, json, boto3

rds = boto3.client('rds', region_name='eu-west-1')
ssm = boto3.client('ssm', region_name='eu-west-1')

pswd = ssm.get_parameter(Name='dbapp', WithDecryption=True)['Parameter']['Value']
host = rds.describe_db_instances(DBInstanceIdentifier='dbapp')['DBInstances'][0]['Endpoint']['Address']
port = rds.describe_db_instances(DBInstanceIdentifier='dbapp')['DBInstances'][0]['Endpoint']['Port']
print("Connecting to: {} on port {} \n".format(host, port))
os.system('mysql -h {} -P {} -u admin -p{}'.format(host, port, pswd))