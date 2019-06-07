import json
import boto3

ddb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # TODO implement

    if event['deviceEvent']['buttonClicked']['clickType'] == 'SINGLE':
        #print('OK')
        scan = ddb.scan(TableName='IoT1Click')
        print(json.dumps(scan))

    elif (event['deviceEvent']['buttonClicked']['clickType'] == 'DOUBLE') and (event['deviceInfo']['attributes']['key3'] == 'value3'):
        get = ddb.get_item(TableName='IoT1Click', Key={'name':{'S': 'first'}}, AttributesToGet=['name'])
        print(json.dumps(get))

    elif (event['deviceEvent']['buttonClicked']['clickType'] == 'LONG'):
        put = ddb.put_item(TableName='IoT1Click', Item={'name':{'S': 'Second'}, 'att': {'N': '30'}})

    else:
        print('Not an expected click')

    return json.dumps(event['deviceEvent']['buttonClicked']['clickType'])
