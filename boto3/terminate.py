import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-088cab4d8bc9e337e').terminate()
