from flask import render_template, request, jsonify
from storageMicroservice.errors import bp

@bp.app_errorhandler(404)
def not_found_error(error):
    responce = jsonify ({'error': 'resource not found'})
    responce.status_code=404
    return responce


@bp.app_errorhandler(500)
def internal_error(error):
    responce = jsonify ({'error': 'internal error'})
    responce.status_code=500
    return responce


@bp.app_errorhandler(400)
def bad_request(message):
    response = jsonify({'error': 'bad request', 'code':400, 'message': message.description})
    response.status_code = 400
    return response


@bp.app_errorhandler(405)
def method_not_allowed(message):
    response = jsonify({'error': 'method not allowed'})
    response.status_code = 405
    return response
