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
        data = request.get_json()
        userid = data.get('userid')
        username = data.get('username')
        password = data.get('password')
        re_password = data.get('re-password')

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

@api.route('/users/<uid>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(uid):
    if request.method == 'GET':
        # get
        user = Fcuser.query.filter(Fcuser.id == uid).first()
        return jsonify(user.serialize)

    elif request.method == 'DELETE':
        # Delete
        Fcuser.query.delete(Fcuser.id == uid)
        return jsonify(), 204       # 204 no content, 정상적으로 삭제되었으니 앞으로 사용할 수 없다는 의미

    # else:
        # 수정

    # Modify
    # put은 전체를 덮는 경향, fetch는 일부를 수정하는 경향이 있다.

    data = request.get_json()
    # type 1. Arrange get data
    # userid = data.get('userid')
    # username = data.get('username')
    # password = data.get('password')

    # updated_data = {}
    # if userid:
    #     updated_data['userid'] = userid
    # if username:
    #     updated_data['username'] = username
    # if password:
    #     updated_data['password'] = password
    # Fcuser.query.filter(Fcuser.id == uid).update(updated_data)
    # type 1. end

    # type 2. put in data on directly
    Fcuser.query.filter(Fcuser.id == uid).update(data)
    # type 2. end 

    user = Fcuser.query.filter(Fcuser.id == uid).first()

    return jsonify(user.serialize)