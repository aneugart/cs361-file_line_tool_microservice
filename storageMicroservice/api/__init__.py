from flask import Blueprint

bp = Blueprint('api', __name__)

from storageMicroservice.api import routes