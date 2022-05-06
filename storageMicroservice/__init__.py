import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from logging.handlers import RotatingFileHandler
from config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    #Init db
    db.init_app(app)
    migrate.init_app(app, db)

    from storageMicroservice.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="")

    from storageMicroservice.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app