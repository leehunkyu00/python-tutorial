import os
from flask import Flask
from flask import session
from flask_jwt import JWT
from flask import render_template
from models import db, Fcuser
from api_v1 import api as api_v1

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix="/api/v1")
# http://localhost:5000/api/v1/test

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def hello():
    print(session.get('userid'))
    return 'hello world! ' + session.get('userid')

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'asvdfvaewfsdcvz'

db.init_app(app)
db.app = app
db.create_all()

# JWT section
## authoticate 함수에 파라미터는 무조건 username, password로 적혀있어야한다.
def authonticate(username, password):
    print("ok ", username, password)
    user = Fcuser.query.filter(Fcuser.userid == username).first()
    if user.password == password:
        return user

jwt = JWT(app, authonticate)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)