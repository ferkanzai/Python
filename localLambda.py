import json
#from __future__ import print_function
#from rx import Observable

def handler(event, context):
    # TODO implement
    print('Hello')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
