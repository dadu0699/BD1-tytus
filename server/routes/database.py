from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS

from parserT28.views.data_window import DataWindow
from parserT28.controllers.error_controller import ErrorController
from parserT28.utils.analyzers.syntactic import parse

dbs = Blueprint('dbs', __name__)

CORS(dbs)


@dbs.route('/create/<name>', methods=['GET'])
def create(name):
    try:
        query = f'CREATE DATABASE IF NOT EXISTS {name};'
        result = parse(query)

        if len(ErrorController().getList()) > 0:
            return {"ok": False}, 400

        result[0].process(0)
        return {"result": DataWindow().data, "ok": True}, 200

    except Exception as e:
        print(e)
        return {"ok": False}, 400


@dbs.route('/showall', methods=['GET'])
def showAll():
    try:
        query = f'SHOW DATABASES;'
        result = parse(query)

        if len(ErrorController().getList()) > 0:
            return {"ok": False}, 400

        result[0].process(0)
        return {"result": DataWindow().data, "ok": True}, 200

    except Exception as e:
        print(e)
        return {"ok": False}, 400
