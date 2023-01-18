import os
import boto3

AMI = os.environ['AMI']                         # ami-0e65ed16c9bf1abc7
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']     # t2.micro
KEY_NAME = os.environ['KEY_NAME']               # ec2-script
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):

    instance = ec2.create_instances(
    ImageId=AMI,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME,
    SubnetId=SUBNET_ID,
    MaxCount=1,
    MinCount=1

)

    print("New instance created:", instance[0].id)