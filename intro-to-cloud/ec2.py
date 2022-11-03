import time
import botocore
import boto3
import paramiko

ec2 = boto3.resource('ec2', region_name='us-east-1')

instance = ec2.create_instances(
    MaxCount=1,
    MinCount=1,
    # change ImageId to your ImageId
    ImageId='ami-09d3b3274b6c5d4aa',
    # change SecurityGroupIds to your SecurityGroupIds
    InstanceType='t2.micro',
    # change Keyname to your KeyName
    KeyName='labdemo-keypair',
    SecurityGroupIds=[
        'sg-0b91ddfa177de9361'
    ],
)

print(instance[0].id)
instance[0].wait_until_running()
print(instance[0].public_ip_address)
time.sleep(15)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.load_system_host_keys()
client.connect(hostname=instance[0].public_ip_address, username="ec2-user", key_filename='<location_of_key>')
stdin, stdout, stderr = client.exec_command(
    'sudo yum install git -y && git clone <repository_name> && sudo bash <location_of_shell.sh>')
print(stdout.readlines())
time.sleep(3)
stdin, stdout, stderr = client.exec_command('python ~/flask-app/app.py &')
print(stdout.readlines())
time.sleep(3)
# client.close()
