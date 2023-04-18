import boto3
from botocore.exceptions import ClientError
import logging

# Variables for AWS credentials

ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXX'

SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Function to upload an item to a DynamoDB table

def upload_item(table, item):

    # Upload the item to the table
    table.put_item(Item=item)
    return
    
# Function to create a DynamoDB table

def create_table(table_name, key_schema, attribute_definitions, provisioned_throughput):
    
    # Create the DynamoDB client
    dynamodb = boto3.client('dynamodb')

    # Create the DynamoDB table
    try:
        dynamodb.create_table(TableName=table_name, KeySchema=key_schema,
                              AttributeDefinitions=attribute_definitions,
                              ProvisionedThroughput=provisioned_throughput)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Lambda function to get the latest file from an S3 bucket, transcripts, and upload it to a DynamoDB table

def lambda_handler(event, context):
    
    # Create the DynamoDB table
    table_name = 'Transcripts'
    key_schema = [
        {
            'AttributeName': 'FileName',
            'KeyType': 'HASH'
        }
    ]
    attribute_definitions = [
        {
            'AttributeName': 'FileName',
            'AttributeType': 'S'
        }
    ]
    provisioned_throughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
    table = create_table(table_name, key_schema, attribute_definitions, provisioned_throughput)
    
    # Upload the latest file to the DynamoDB table
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('transcripts')
    latest_file = bucket.objects.all().order_by('-last_modified').first()
    item = {
        'FileName': latest_file.key
    }
    upload_item(table, item)
    
    return




