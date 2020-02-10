# This script will be used to create table in the database
# We are using generic attribute names like PK for partition key and SK for sort key in this script


import boto3

dynamodb = boto3.client('dynamodb')

try:
    dynamodb.create_table(
        TableName='quick-photos',
        AttributeDefinitions=[
            {
                "AttributeName": "PK",
                "AttributeType": "S"
            },
            {
                "AttributeName": "SK",
                "AttributeType": "S"
            }
        ],
        KeySchema=[
            {
                "AttributeName": "PK",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "SK",
                "KeyType": "RANGE"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )
    print("Table created successfully.")
except Exception as e:
    print("Could not create table. Error:")
    print(e)
