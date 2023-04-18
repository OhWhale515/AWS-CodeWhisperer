# Function to upload an object to s3 and return the object's URL

import boto3
import botocore
import os
import logging

s3 = boto3.client('s3')

def upload_file_to_s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    try:
        response = s3.upload_file(file_name, bucket, object_name)
    except botocore.exceptions.ClientError as e:
        logging.error(e)
        return False
    return True
    
def main():
    # Upload a file to S3
    upload_file_to_s3('test.txt', 'testbucket')
    
if __name__ == '__main__':
    main()
    