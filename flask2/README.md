
# Build Environment
## 가상환경 만들기
### Windows
$ virtualenv flask_rest
$ .\flask_rest\Scripts\activate.ps1  

### mac & linux
$ virtualenv flask_rest
$ source .\flask_rest\bin\activate

## Install flask

(flask_rest) PS [path]> pip install flask

### source
app.py file

## Install flask-sqlalchemy
(flask_rest) PS [path]> pip install flask-sqlalchemy

### source
model.py file

## Install flask-JWT
(flask_rest) [path]> pip install Flask-JWT

# API 만들기
blue code란걸 사용해서 api을 관리한다.

## 과정
api.v1을 만들고 app.py에 등록을 한다.

```
from api_v1 import api as api_v1

app.register_blueprint(api_v1, url_prefix="/api/v1")
```
http://localhost:5000/api/v1/test


### source
api.v1 folder
