Serverless api based login to ecr
-----------------------------------

This is a simple function based on kubeless and python. It gets the value of the ECR token from AWS and sends it to kubernetes. 
For security reasons all the credentials are given to the container as enviromental variables. This is intended more or less as a cronjob. 

1. How-to

```
export aws_access_key_id=<AWSACCESSKEYABCDEF>
export aws_secret_access_key=<YOUR+KEY+HERE>
```

Parse your k8s configuration as a secret as well. 

2. To do!!!
Make it do more - force a docker login on the K8S cluster. 