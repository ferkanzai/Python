import boto3
import json

token = None

org = boto3.client('organizations')
paginator = org.get_paginator('list_accounts')

account_list = []

# Using the list_accounts client method

while True:
    if token:
        response_iterator = org.list_accounts(
            MaxResults = 20,
            NextToken = token
        )
    else:
        response_iterator = org.list_accounts(
            MaxResults = 20
        )
    for account in response_iterator['Accounts']:
        print(account['Id'])
        print(account['Name'])
        account_list.append({
            'account_id': account['Id'],
            'account_name': account['Name']
            }
        )
    try:
        token = response_iterator['NextToken']
        print(token)
    except KeyError:
        break

# Using the paginate method of the paginator

while True:
    if token:
        response_iterator = paginator.paginate(
            PaginationConfig = {
                'MaxItems': 20,
                'PageSize': 20,
                'NextToken': token
            }
        )
    else:
        response_iterator = paginator.paginate(
            PaginationConfig = {
                'MaxItems': 20,
                'PageSize': 20
            }
        )
    for page in response_iterator:
        accounts = page['Accounts']
        for account in accounts:
            print(account['Id'])
            print(account['Name'])
        account_list.append({
            'account_id': account['Id'],
            'account_name': account['Name']
            }
        )
    try:
        token = page['NextToken']
        print(token)
    except KeyError:
        break

print(json.dumps(account_list, indent=2))