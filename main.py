import importlib
import os

from flask import Flask, jsonify

import api_views
from config import config, Config


def create_app():
    application = Flask(__name__)
    application.config.from_pyfile(".env", silent=False)
    for i in application.config:
        os.environ[i] = str(application.config[i])
    
    return application


def init_api(application):
    for i in application.config:
        os.environ[i] = str(application.config[i])

    for path, blueprint, url_prefix in api_views.blueprints:
        module = importlib.import_module(path)
        application.register_blueprint(getattr(module, blueprint), url_prefix=url_prefix)

    return application
