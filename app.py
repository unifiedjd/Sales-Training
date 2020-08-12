import json
import datetime
import os
import time
import requests

from flask import Flask, request, Response, jsonify
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    # return default response
    name = request.args.get('name')
    if name == None:
        name = 'Lenny & Reid'
    return Response("<html><body>Welcome to your training, {name}!</body></html>".format(name=name), status=200)