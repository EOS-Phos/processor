from flask import Flask, request
from npre import bbs98
import zipfile

app = Flask(__name__)
pre = bbs98.PRE()

@app.route('/proxy-re-encrypt')
def pre():
    filename = request.args.get('filename', default = "", type = str)
    # load the zip file and unpack
    file_data = zipfile.ZipFile(load_file_data_from_s3(input_filename))

    for name in file_data.namelist():
        data = file_data.read(name)
        encrypted_data_a = data['photo']
        for (rk, pk) in data['proxy_keys']:
            encrypted_data_b = pre.reencrypt(rk, encrypted_data_a)
            unique_filename = "{}-{}.d33p".format(hash(encrypted_data_a), hash(pk))
            save_file_data_to_s3(encrypted_data_b, unique_filename)
            

#todo: https://github.com/ipfs/py-ipfs-api


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
