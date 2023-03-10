# Lets create EC2 instances using Python BOTO3
import boto3


def create_ec2_instance():
    """
    MaxCount=1, # Keep the max count to 1, unless you have a requirement to increase it
    InstanceType="t2.micro", # Change it as per your need, But use the Free tier one
    KeyName="ec2-key" # Change it to the name of the key you have.
    :return: Creates the EC2 instance.
    """
    try:
        print ("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-0b84fc3f0121dbe00",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="EC2-key"
        )
    except Exception as e:
        print(e)

create_ec2_instance()