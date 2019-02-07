"""creates an instance of a flask application and runs it"""
from flask import Flask
from instance.config import config

def create_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)
    # from app.api.v1.views.routes import api
    from .api.v1.views.views import api as version1
    app.register_blueprint(version1)
    return app