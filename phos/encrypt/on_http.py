import json
import boto3
BUCKET = os.environ['S3_BUCKET']


def main(event, context):

    print(context)
    print(context["requestContext"])
    if context["requestContext"]["httpMethod"] == "GET":
        get_data = json.loads(context['pathParameters'])
        print(get_data)

    file_name = "my-new-path-name"

    get_url = "http://{bucket}.s3.amazonaws.com/{object}".format(
                bucket=BUCKET, object=key)

    in_file = open("in-file", "rb") # opening for [r]eading as [b]inary
    data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
    in_file.close()

    s3 = boto3.resource('s3')
    bucket = s3.Bucket("eos-phos-dev")
    path = 'my-new-path-name.txt'

    bucket.put_object(
        ACL='public-read',
        ContentType='application/json',
        Key=path,
        Body=data,
        )



    body = {}
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
