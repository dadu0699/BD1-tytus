from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS
import simplejson as json

from parserT28.parse import execution

dbs = Blueprint('dbs', __name__)

CORS(dbs)


@dbs.route('/create/<name>', methods=['GET'])
def create(name):
    try:
        query = f'CREATE DATABASE IF NOT EXISTS {name};'

        result = execution(query)
        result = json.loads(json.dumps(result, ignore_nan=True))

        return {"result": result, "ok": True}, 200

    except Exception as e:
        print(e)
        return {"ok": False}, 400


@dbs.route('/showall', methods=['GET'])
def showAll():
    try:
        query = f'SHOW DATABASES;'

        result = execution(query)
        result = json.loads(json.dumps(result, ignore_nan=True))

        print(result['querys'][0][1])

        return {"result": result['querys'][0][1], "ok": True}, 200

    except Exception as e:
        print(e)
        return {"ok": False}, 400
