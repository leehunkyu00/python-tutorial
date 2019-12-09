from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.validators import  DataRequired, EqualTo

class RegisterForm(FlaskForm):
    # 입력받고자 하는 필드를 여기에 만들면 된다.
    userid = StringField('userid', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired(), EqualTo('repassword')])
    repassword = StringField('repassword', validators=[DataRequired()])