# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
app = Flask(__name__)
from pyteaser import SummarizeUrl
import urllib2
import json

@app.route('/summarize', methods=['GET'])
def summarize():
    url = urllib2.unquote(request.args.get('u') or '');
    summaries = SummarizeUrl(url)
    return jsonify(result=summaries)

# Default hello template from serverless which is useless now because we're
# serving off our endpoints via Flask + serverless-wsgi
def hello(event, context):
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
"""
if __name__ == "__main__":
    #main('', '')
    app.run(host='127.0.0.1', port=8080, debug=True)
"""
