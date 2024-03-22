import requests
import flask
from flask import Flask, jsonify

app = flask.Blueprint("api_healthcheck", __name__)


@app.route('/healcheck', methods=['GET'])
def healcheck():
    check = False
    url = 'http://127.0.0.1:8000/'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return jsonify({
                'status': "success"
            }), 200
        else:
            return jsonify({
                'status': "faild"
            }), 500
    except Exception as e:
        return jsonify({
                'status': "faild"
            }), 500

# if __name__ == '__main__':
#     app.run(debug=True)