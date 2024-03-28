from flask import Flask, jsonify
from Tuan02.api.service import app as api_service
from Tuan02.api.healcheck import app as api_healthcheck
from Tuan02.api.profile import app as profile
from api_dto.api_exeption import *

app = Flask(__name__)
app.register_error_handler(Exception, error_handler)
app.register_blueprint(api_service, url_prefix='/B1')
app.register_blueprint(api_healthcheck, url_prefix='/B1')
app.register_blueprint(profile, url_prefix='/B3')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)