# FastCampus강의

## Environment
$ sudo pip install virtualenv

$ virtualenv flask_fastcampus
$ source flask_fastcampus/bin/activate
$ pip install flask

> window cmd의 경우 
> $ call flask_fastcampus/bin/activate
> window powershell의 경우 
> .\flask_fastcampus\Scripts\activate.ps1

## Hello world!
### code
app.py

### Run
$ FLASK_APP=app.py flask run

__main__을 동작하게 하려면, 
$ python app.py

## MVC 패턴
Model, View, Controller

## 
SQLAlchemy을 쉽게 사용할 수 있게 flask로 만들어진 것
$ pip install flask-sqlalchemy

## template
jinja template engine

# 회원가입 기능 만들기
## get/post 받기
from flask import request


# Flask-WTF 사용
마이크로 프레임 워크로 Flask는 많은 기능이 없는데 폼관리를 할때는 Flask-WTF을 주로 사용한다.

## 설치
$ pip install Flask-WTF

## 사용방법
form을 대체하는 템플릿을 만들어서 주로 사용한다

1. forms.py을 작성

2. CSRF을 설정해야한다.
사이트 간 요청 위조(Cross-site request)
form안에 hash키를 넣어놓고 입력받은 form에 hash을 비교하여 맞는지 확인

form html안에 {{ form.csrf_token }}

3. 유효성 검사를 해주는 기능이 있어서 사용할 수 있다.


# static file 관리하기
file들을 flask에서 관리하는 방법

static 폴더를 만들어서 여기에 넣으면 끝.
static 하위 경로로 사용하면 된다.

# login/logout 만들기
from flask import session 을 이용해서 만든다.

여기서 주의할 점은 validators에 사용자 정의 클래스의 실패시 return하는 값은
return으로 쓰는게 아니라 raise로 쓴다.

코드를 보면 특이한걸 알 수 있다.


# python anywhere


file을 upload한 뒤

bash shell을 열어서 아래와 같이 설정한다.
06:14 ~ $ virtualenv --python=python3.7 flask_fastcampus
06:15 ~ $ source flask_fastcampus/bin/activate
(flask_fastcampus) 06:15 ~ $ pip install flask flask-wtf flask-sqlalchemy

web으로 가서 'Add a new web app'을 선택한다.
manual config로 python 3.7선택

코드 위치설정
project directory path 설정
/home/leehunkyu00/[project dir]

leehunkyu00_pythonanywhere_com_wsgi.py 수정
```
import sys

# The "/home/leehunkyu00" below specifies your home
# directory -- the rest should be the directory you uploaded your Flask
# code to underneath the home directory.  So if you just ran
# "git clone git@github.com/myusername/myproject.git"
# ...or uploaded files to the directory "myproject", then you should
# specify "/home/leehunkyu00/myproject"
path = '/home/leehunkyu00/project'
if path not in sys.path:
    sys.path.append(path)

from app import app as application  # noqa
```

가상환경 설정
/home/leehunkyu00/[virtual path]