import flask
from flask import Flask, jsonify

app = flask.Blueprint("api_service", __name__)
    
@app.route('/', methods=['GET'])
def service():
    print("API service")
    response = jsonify()
    response.status_code = 200
    return response