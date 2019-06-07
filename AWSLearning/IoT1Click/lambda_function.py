import json
import boto3

ddb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # TODO implement

    if event['deviceEvent']['buttonClicked']['clickType'] == 'SINGLE':
        print('OK')
        scan = ddb.scan(TableName='TheBikeShop-BikeTable')
        print(json.dumps(scan))

    elif (event['deviceEvent']['buttonClicked']['clickType'] == 'DOUBLE') and (event['deviceInfo']['attributes']['key3'] == 'value3'):
        get = ddb.get_item(TableName='TheBikeShop-BikeTable', Key={'model':{'S': 'FirstBike'}}, AttributesToGet=['name', 'colour', 'price'])
        print(json.dumps(get))
        return "{} is {} and cost ${}".format(get['Item']['name']['S'], get['Item']['colour']['S'], get['Item']['price']['N'])

    else:
        print('Not an expected click')

    return json.dumps(event['deviceEvent']['buttonClicked']['clickType'])
