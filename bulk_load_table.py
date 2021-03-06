# This script will be used to bulk load the json file into the table

import json

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('quick-photos')

items = []

with open('scripts/items.json', 'r') as f:
    for row in f:
        items.append(json.loads(row))

with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)
