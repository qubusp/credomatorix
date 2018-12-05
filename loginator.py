import boto3
import simplejson as json
from base64 import b64decode
from kubernetes import client, config
from pprint import pprint
import docker



ecr = boto3.client('ecr',
    region_name='eu-west-1'
)

response = ecr.get_authorization_token()
raw_data=response['authorizationData'][0]['authorizationToken']
user, decoded_data=b64decode(raw_data).decode('UTF-8').split(":")
docker_client = docker.from_env()
docker_client.login(username='AWS', password=decoded_data, registry='163690719035.dkr.ecr.eu-west-1.amazonaws.com')
