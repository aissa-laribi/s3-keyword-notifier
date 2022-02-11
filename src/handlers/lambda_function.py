import boto3
import time
import sys
import urllib.parse

import json

print('Loading function')

s3 = boto3.client('s3')
#Use a gmail.com preferably
VERIFIED_EMAIL = '<Your_verified_email>'

ses = boto3.client('ses')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    response = s3.get_object(Bucket=bucket, Key=key)
    body = s3.get_object(Bucket=bucket, Key=key)['Body'].read().decode('utf-8')
    def keyword_finder(word):
        if word in body:
            print("word found")
            ses.send_email(
                Source=VERIFIED_EMAIL,
                Destination={
                    'ToAddresses': ['<your_destination_verified_email']  # Also a verified email
                },
                Message={
                    'Subject': {'Data': 'A new %s file has been uploaded!'% (word)},
                    'Body': {'Text': {'Data': 'Hi there!,\n\n A new file with the %s keyword has just been uploaded in your %s bucket!\n\n Have a Lovely day!'% (word,bucket)}}
                    }
            )
        else:
            print("nothing")
    keyword_finder('<your_keyword>')
    return json.dumps(keyword_finder,default=str)
