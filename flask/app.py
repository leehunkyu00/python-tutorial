import os
from flask import Flask
from flask import request           # 요청 정보 확인용
from flask import redirect
from flask import render_template
from models import db

from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm

from models import Fcuser

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()
    print(request.method)
    # get, post 인지 확인해야함

    # Type 1. pure python
    # if request.method == 'POST':
    #     # 가입 form
    #     userid = request.form.get('userid')
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     re_password = request.form.get('re-password')

    #     print(userid, username, password, re_password, password, re_password)
    #     # 모든 값이 있는지
    #     if (userid and username and password and re_password) and password == re_password:
    #         fcuser = Fcuser()
    #         fcuser.userid = userid
    #         fcuser.username = username
    #         fcuser.password = password

    #         db.session.add(fcuser)
    #         db.session.commit()

    #         return redirect('/')

    # Type 2. Using wtform
    if form.validate_on_submit():
        # post요청이고, 안의 데이터들이 유효성 검사인지 확인하는 함수
        fcuser = Fcuser()
        fcuser.userid = form.data.get('userid')
        fcuser.username = form.data.get('username')
        fcuser.password = form.data.get('password')

        db.session.add(fcuser)
        db.session.commit()
        print('Success!')

        return redirect('/')

    return render_template('register.html', form=form)

@app.route('/')
def hello():
    # return 'Hello World'
    # Find source from ./templates folder
    return render_template('hello.html')

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'asvdfvaewfsdcvz'

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)
    db.app = app
    db.create_all()

    app.run(host='127.0.0.1', port='5000', debug=True)