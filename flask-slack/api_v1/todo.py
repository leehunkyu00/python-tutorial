from flask import jsonify
from flask import request
import requests

from . import api

# todo app
@api.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'POST':
        res = requests.post('https://hooks.slack.com/services/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', json={
            'text': 'hello world!'
        }, headers={'Content-Type': 'application/json'})
        # TEST >curl -X POST -H 'Content-type: application/json' http://localhost:5000/api/v1/todos
    elif request.method == 'GET':
        pass

    data = request.get_json()
    return jsonify(data)

# slack test - slash command
@api.route('/test', methods=['POST'])
def test():
    res = request.form['text']
    print(res)
    return jsonify(res)