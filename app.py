import json

from flask import Flask, request, Response, jsonify
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    name = request.args.get('name')
    if name == None:
        name = 'Lenny & Reid * Ben'
    return Response("<html><body>Welcome to your training, {name}!</body></html>".format(name=name), status=200)