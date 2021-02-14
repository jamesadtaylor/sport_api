"""API Test Class"""
import json

import requests
from flask import Flask, jsonify

from flask_swagger import swagger

from sports.config import URL_LAST_FIVE_RESULTS
from sports.fixture import Fixture

app = Flask(__name__)


@app.route('/')
def blank() -> str:
    """hello world method"""
    return "Nothing here!!!"


@app.route("/spec")
def spec():
    """stub for swagger end points"""
    return jsonify(swagger(app))


@app.route('/previousfivegames')
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
    app.run()
