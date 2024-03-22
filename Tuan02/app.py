from flask import Flask
from api.B1_service import app as api_service
from api.B1_healcheck import app as api_healthcheck
from api.B3_profile import app as profile
from api_dto.api_exeption import error_handler

app = Flask(__name__)
app.register_error_handler(Exception, error_handler)
app.register_blueprint(api_service, url_prefix='/B1')
app.register_blueprint(api_healthcheck, url_prefix='/B1')
app.register_blueprint(profile, url_prefix='/B3')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)