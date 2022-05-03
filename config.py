import os

class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    LOGS_DIR = os.path.join(BASE_DIR, "logs")
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET_KEY_HERE!!!3546541'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
