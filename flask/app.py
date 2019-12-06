import os
from flask import Flask
from flask import request           # 요청 정보 확인용
from flask import redirect
from flask import render_template
from models import db

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():

    print(request.method)
    if request.method == 'GET':
        # 화면 form
        return render_template('register.html')
    else:
        # 가입 form
        return redirect('/')


    # get, post 인지 확인해야함

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

    db.init_app(app)
    db.app = app
    db.create_all()

    app.run(host='127.0.0.1', port='5000', debug=True)