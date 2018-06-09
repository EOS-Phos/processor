import json
import boto3
import requests


in_file = open("image.jpg", "rb") # opening for [r]eading as [b]inary
data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

s3 = boto3.resource('s3')
bucket = s3.Bucket("eos-phos-dev")
path = 'my-path-name.txt'

bucket.put_object(
    ACL='public-read',
    ContentType='application/json',
    Key=path,
    Body=data,
    )
