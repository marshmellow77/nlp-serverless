
import os
import io
import boto3
import json
import csv


ENDPOINT_NAME = "hf-serverless-ep2021-12-23-10-42-53"
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Body=json.dumps(event, indent=4))
    result = json.loads(response['Body'].read().decode())
    pred = result[0]['label']

    return pred
