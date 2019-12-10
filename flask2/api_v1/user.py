from flask import jsonify
from flask import request
from models import Fcuser, db
from . import api
# json 형태의 데이터를 반환

@api.route('/test')
def test():
    return jsonify(), 404

@api.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re-password')

        if not (userid and username and password and re_password):
            return jsonify({'error': 'No arguments'}), 400

        if password != re_password:
            return jsonify({'error': 'Wrong password'}), 400

        fcuser = Fcuser()
        fcuser.userid= userid
        fcuser.username = username
        fcuser.password = password

        db.session.add(fcuser)
        db.session.commit()

        return jsonify(), 201

    users = Fcuser.query.all()
    # 직렬화를 위해서 모델 안에 리턴해주는 포맷을 만든 후 진행형 리스트로 만들어서 전달한다.

    # type 1. 만든 후 return
    # res_users = []
    # for user in users:
    #     res_users.append(user.serialize)
    # return jsonify(res_users)

    # type 2. 진행형 리스트
    return jsonify([user.serialize for user in users])