"""API Test Class"""
import json

import requests
from flask import Flask, jsonify

from flask_swagger import swagger

from config import URL_LAST_FIVE_RESULTS
from fixture import Fixture

server = Flask(__name__)


@server.route('/')
def blank() -> str:
    """hello world method"""
    return "Nothing here!!!"


@server.route("/spec")
def spec():
    """stub for swagger end points"""
    return jsonify(swagger(server))


@server.route('/previousfivegames')
def last_leeds_5_games():
    """
    Returns the last 5 results Leeds United played
    ---
    """
    response = requests.get(URL_LAST_FIVE_RESULTS + '?id=133635')
    return transform_response(response.json())


def transform_response(_json: dict) -> str:
    """Transform message format from sports db to lite version for display via API"""
    my_list = dict(_json).pop("results")
    converted_list = []
    for fix in my_list:
        converted_list.append(Fixture(fix))
    return json.dumps([f.dump() for f in converted_list])


if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0')
