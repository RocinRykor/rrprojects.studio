from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms import BooleanField
from wtforms.validators import InputRequired, Length, EqualTo
from wtforms.widgets import TextArea


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(),
                                                   Length(max=30)])
    password = PasswordField("Password", validators=[InputRequired(),
                                                     Length(min=12)])
    submit = SubmitField("Login")