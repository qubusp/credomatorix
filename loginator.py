import boto3 
import simplejson as json 
from base64 import b64decode
from kubernetes import client, config
from pprint import pprint
ecr = boto3.client('ecr',
    region_name='eu-central-1'
)


response = ecr.get_authorization_token()
raw_data=response['authorizationData'][0]['authorizationToken']
user, decoded_data=b64decode(raw_data).decode('UTF-8').split(":")


config.load_kube_config()
v1 = client.CoreV1Api()
namespace = 'default'
metadata = {'name': 'aws-login', 'namespace': 'default'}
data = {'user': 'AWS', 'token': decoded_data}
api_version = 'v1'
kind = 'Secret'
body = client.V1Secret(api_version, data , kind, metadata, type='kubernetes.io/tls')
api_response = v1.create_namespaced_secret(namespace, body, async=True)
pprint(api_response)

