import json
import boto3
BUCKET = os.environ['S3_BUCKET']

def reencrypt_on_s3_upload(event, context):
    import requests

    logger.debug('event: {}'.format(event))
    event_name = event['Records'][0]['eventName']
    key = event['Records'][0]['s3']['object']['key']

    try:
        if 'ObjectCreated:Put' == event_name:

            try:
                # connect to s3
                s3 = boto3.client('s3')

                # what is the download url of the file?
                get_url = "http://{bucket}.s3.amazonaws.com/{object}".format(
                                bucket=BUCKET, object=key)

                # download the data from the url
                r = requests.get(get_url)
                data = r.content


                # save the data to another filename
                path = 'my-path-name.txt'

                # upload to the S3 bucket
                s3 = boto3.resource('s3')
                bucket = s3.Bucket(BUCKET)
                bucket.put_object(
                    ACL='public-read',
                    ContentType='application/json',
                    Key=path,
                    Body=data,
                    )

            except Exception:
                return {
                    'statusCode': httplib.BAD_REQUEST,
                    'body': {
                        'error_message': 'Unable to complete'}
                }

    except DoesNotExist:
        return {
            'statusCode': httplib.NOT_FOUND,
            'body': {
                'error_message': 'ASSET {} not found'.format(asset_id)
            }
        }

    return {'statusCode': httplib.ACCEPTED}

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def reencrypt_on_http_request(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
