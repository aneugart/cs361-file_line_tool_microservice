from storageMicroservice.api import bp
from flask import abort, Response
from flask.json import jsonify

@bp.route('/', methods=['GET'])
def get_all_entries():
    test= {"data":"Hello World!"}

    return jsonify(test), 200