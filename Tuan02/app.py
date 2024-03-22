from flask import Flask
from api.B1_service import app as api_service
from api.B1_healcheck import app as api_healthcheck
from api.B3_api import app as api_app

app = Flask(__name__)
app.register_blueprint(api_service, url_prefix="/")
app.register_blueprint(api_healthcheck, url_prefix="/")
app.register_blueprint(api_app, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)