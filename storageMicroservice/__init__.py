import os
import logging
from flask import Flask
from logging.handlers import RotatingFileHandler
from config import Config


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    from storageMicroservice.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="")

    return app