# Phos Processor for D3EP
### Run a client processor node via Flask app or via serverless functions

# running with Flask and testing locally

if not familiar with Flask, check out http://flask.pocoo.org/docs/1.0/quickstart/

```
$ pip install Flask
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

# running with Serverless Framework, AWS Lmabda

if new, read https://serverless.com/framework/docs/

```
cd /phos
sls deploy -v
* endpoints:
  GET - https://zarstax6f.execute-api.us-east-1.amazonaws.com/dev/reencrypt

sls logs -f reencrypt_on_http_request -t
```
