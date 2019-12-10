from flask import jsonify
from flask import request
from flask import session
from flask import redirect
from models import Fcuser, db
from . import api

@api.route('/login', methods=['POST'])
def login():
    if (request.method == 'POST'):
        data = request.get_json()

        userid = data.get('userid')
        password = data.get('password')

        if not (userid and password):
            return jsonify(), 404

        user = Fcuser.query.filter(Fcuser.userid == userid).first()

        print(user.password, password)
        if user.password == password:
            print("session!", userid)
            session['userid'] = userid
            return jsonify()

        return jsonify(), 404
