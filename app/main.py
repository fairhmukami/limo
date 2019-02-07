from flask import Flask

def create_app(config_file):
    app=Flask(__name__)
    app.config.from_object(config_file)
    from app.api.v1.views.views import api
    app.register_blueprint(api, url_prefix='/api/v1')
    return app