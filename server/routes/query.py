from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS
import simplejson as json

from parserT28.parse import execution

qry = Blueprint('qry', __name__)
CORS(qry)


@qry.route('/exec', methods=['POST'])
def exec():
    """Ejecuta una consulta y devuelve el resultado"""
    # Recupera la consulta a ejecutar
    body = request.get_json()
    query = body.get('query')
    try:
        # Ejecuta el query (con el interpreter)
        result = execution(query)
        result = json.loads(json.dumps(result, ignore_nan=True))
        return {"result": result, "ok": True}, 200
    except Exception as e:
        #  Retorna un mensaje de error en el servidor
        print(e)
        return {"ok": False}, 400
