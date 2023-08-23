import boto3
import json
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):

    # Connect to dynamodb service
    dynamodb = boto3.resource(
        'dynamodb'
    )
    
    # Connect to table
    table = dynamodb.Table('Restaurant')
    menu = table.query(
        KeyConditionExpression=Key('Type').eq('Appetizer')
    )
    
    return menu["Items"]