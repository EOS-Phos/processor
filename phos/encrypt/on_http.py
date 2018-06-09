import os
import json
import boto3
import requests
from io import BytesIO

BUCKET = os.environ["BUCKET"]

# npx sls invoke local -f reencrypt_on_http_request --data '{"filename":"my-path-name.txt"}'

def main(event, context):

    # file names
    input_filename = event["filename"]
    output_filename = 'my-new-path-name.txt'

    # download file
    get_url = "http://{bucket}.s3.amazonaws.com/{object}".format(
                bucket=BUCKET, object=input_filename)

    response = requests.get(get_url)
    img_data = BytesIO(response.content)

    # setup S3 connection
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET)

    # do something magical

    # save new file in the bucket
    bucket.put_object(
        ACL='public-read',
        ContentType='application/json',
        Key=output_filename,
        Body=img_data,
        )

    new_url = "http://{bucket}.s3.amazonaws.com/{object}".format(
                        bucket=BUCKET, object=output_filename)

    body = {
        "input_file":input_filename,
        "output_file": output_filename
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
