import os
import json
import boto3
import requests
from io import BytesIO

BUCKET = os.environ["BUCKET"]

# npx sls invoke local -f reencrypt_on_http_request --data '{"filename":"my-path-name.txt"}'

def main(event, context):

    # get file from s3
    input_filename = event["filename"]
    file_data = load_file_data_from_s3(input_filename)


    filename = request.args.get('filename', default = "", type = str)
    # load the zip file and unpack
    file_data = zipfile.ZipFile(load_file_data_from_s3(input_filename))

    output_filenames = []

    # iterate through files in zipfile
    for name in file_data.namelist():
        data = file_data.read(name)
        encrypted_data_a = data['photo']

        # reencrypt for each reencryption key pair
        # todo: these can run in parallel, not serialized
        for (rk, pk) in data['proxy_keys']:
            encrypted_data_b = pre.reencrypt(rk, encrypted_data_a)
            unique_filename = "{}-{}.d33p".format(hash(encrypted_data_a), hash(pk))
            # Save file to s3
            save_file_data_to_s3(encrypted_data_b, unique_filename)
            output_filenames.append(unique_filename)


    body = {
        "input_file": input_filename,
        "output_file": output_filenames
    }
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }


def load_file_data_from_s3(input_filename):
    # download file
    get_url = "http://{bucket}.s3.amazonaws.com/{object}".format(
                bucket=BUCKET, object=input_filename)

    response = requests.get(get_url)
    file_data = BytesIO(response.content)
    return file_data


def save_file_data_to_s3(file_data, output_filename):
    # setup S3 connection
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET)

    # save new file in the bucket
    bucket.put_object(
        ACL='public-read',
        ContentType='application/json',
        Key=output_filename,
        Body=file_data,
        )

    new_url = "http://{bucket}.s3.amazonaws.com/{object}".format(
                        bucket=BUCKET, object=output_filename)

    return
