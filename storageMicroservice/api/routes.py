from flask import abort, request
from flask.json import jsonify
import datetime as dt
from storageMicroservice.models import date_keywords
from storageMicroservice.api import bp
from storageMicroservice import db

@bp.route('/', methods=['GET'])
def get_all_records():
    """
    Get all records from the database.
    
    :return: 200
    """
    data= {"data":{}}
    entries = date_keywords.query.all()
    for entry in entries:
        data["data"][entry.date.strftime("%Y-%m-%d")] = entry.keyword
    return jsonify(data), 200


@bp.route('/<the_date>', methods=['GET'])
def get_record_by_date(the_date):
    """
    Get a single entry from the database

    :param str the_date: The date of the entry to get (format:  "YYYY-MM-DD")
    :return: 200 if successful, 400 or 404 there is an error.
    """
    # Confirm that "the_date" may be parsed as a date.
    try:
        date = dt.datetime.strptime(the_date, "%Y-%m-%d").date()
    except ValueError:
        abort(400, description="Invalid date entered.  Date must be YYYY-MM-DD")
    entry = date_keywords.query.filter(date_keywords.date == the_date).first()
    # Return an error if the entry does not exist
    if entry is None:
        abort(404)
    # If the entry was found, return it
    responce = jsonify({"data":{entry.date.strftime("%Y-%m-%d"):entry.keyword}})
    responce.status_code = 200
    return responce


@bp.route('/', methods=['POST'])
def create_record():
    """
    Create a new entry and save it to the datebase.

    :return: 201 if successful, 400 or 500 if there is an error.
    """
    print(request.content_type , request.content_type == "application/jsond")
    # Confirm that the content-type is "application/json".
    if request.content_type != "application/json":
        abort(400, description="Content-type MUST be application/json")
    content_body = request.get_json()
    # Confirm that the body contains "date" and "keyword" keys.
    if "date" not in content_body.keys() or "keyword" not in content_body.keys():
        abort(400, description="JSON object MUST contain date and keyword keys!.")
    # Confirm that the "date" key may be parsed as a date.
    try:
        date = dt.datetime.strptime(content_body["date"], "%Y-%m-%d").date()
    except ValueError:
        abort(400, description="Invalid date entered.  Date must be YYYY-MM-DD")
    # Confirm that the no entries with the given date exist in the DB.
    entries = date_keywords.query.filter(date_keywords.date == date).first()
    if entries is not None:
        abort(400, description="an entry with for this date already exists!")
    # After all of our tests, add to the DB
    try:
        new_entry = date_keywords(date=date, keyword=content_body["keyword"])
        db.session.add(new_entry)
        db.session.commit()
    except:  # If the creation fails, rollback DB changes and send 500 error
        db.session.rollback()
        abort(500)
    responce = jsonify({"date":date.strftime("%Y-%m-%d"), "keyword": content_body["keyword"]})
    responce.status_code = 201
    return responce


@bp.route('/<the_date>', methods=['DELETE'])
def delete_record(the_date):
    """
    Delete a single entry from the database.

    :param str the_date: The date of the entry to be deleted (format:  "YYYY-MM-DD")
    :return: 204 if successful, 400, 404, or 500 if there is an error.
    """
    # Confirm that "the_date" may be parsed as a date.
    try:
        date = dt.datetime.strptime(the_date, "%Y-%m-%d").date()
    except ValueError:
        abort(400, description="Invalid date entered.  Date must be YYYY-MM-DD")
    entry = date_keywords.query.filter(date_keywords.date == the_date).first()
    # Return an error if the entry does not exist
    if entry is None:
        abort(404)
    # If an entrty is found, delete it.
    try:
        date_keywords.query.filter(date_keywords.date == the_date).delete()
        db.session.commit()
    except:  # If the deleation fails, rollback DB changes and send 500 error
        db.session.rollback()
        abort(500)
    return {}, 204
