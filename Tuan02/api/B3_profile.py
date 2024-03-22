from flask import Flask, request, jsonify
from handler import bootstrap

import flask

app = flask.Blueprint("profile", __name__)

@app.route('/data/profile', methods=['POST'])
def read_infor():
    name = request.form['name']
    data = bootstrap.get_data_profile(name=name)
    return data