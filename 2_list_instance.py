def list_all_instances():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        print("Id: {0}".format(instance.id))

list_all_instances()