
#Function to spin up an EC2 instance and return the instance ID

import boto3

def create_instance():
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId='ami-0e3b5a9b5e7c1a6c5',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='ec2-keypair'
        )
    print(instance[0].id)
    return instance[0].id
    
#Function to terminate an EC2 instance

def terminate_instance(instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    instance.terminate()
    print("Instance terminated")
    
    
# Function to apply cloudwatch logs to an EC2 instance

def apply_cloudwatch_logs(instance_id):
    cloudwatch = boto3.client('logs')
    cloudwatch.create_log_group(logGroupName='ec2-logs')
    cloudwatch.create_log_stream(logGroupName='ec2-logs', logStreamName='ec2-logs')
    cloudwatch.put_log_events(logGroupName='ec2-logs', logStreamName='ec2-logs', logEvents=[
        {
            'timestamp': 123456789,
            'message': 'This is a test message'
        }
        ], sequenceToken='STRING_VALUE')
