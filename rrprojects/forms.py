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

class ProjectForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired(), Length(max=64)])
    repo_link = StringField("GitHub URL", validators=[InputRequired(), Length(max=256)])
    live_link = StringField("Live URL", validators=[InputRequired(), Length(max=256)])
    description = TextAreaField("Description", validators=[InputRequired(), Length(max=8192)])
    img_filename = StringField("Project IMG", validators=[InputRequired(), Length(max=128)])

    submit = SubmitField("Add Project")   