from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, FileField
from wtforms.validators import InputRequired, Length, EqualTo, DataRequired
from wtforms.widgets import TextArea


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(),
                                                   Length(max=30)])
    password = PasswordField("Password", validators=[InputRequired(),
                                                     Length(min=12)])
    submit = SubmitField("Login")

class ProjectForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired(), Length(max=64)])
    repo_link = StringField("Repository URL", validators=[InputRequired(), Length(max=256)])
    repo_link_description = StringField("Repository Descripion", validators=[InputRequired(), Length(max=256)], default="Check out the project on GitHub!")
    live_link = StringField("Live URL", validators=[InputRequired(), Length(max=256)])
    live_link_description = StringField("Repository Descripion", validators=[InputRequired(), Length(max=256)], default="View the live version here!")
    short_description = TextAreaField("Card Description", validators=[InputRequired(), Length(max=256)])
    description = TextAreaField("Page Description", validators=[InputRequired(), Length(max=8192)])
    img_filename = StringField("Project IMG", validators=[InputRequired(), Length(max=128)], default="placeholder.png")

    submit = SubmitField("Add Project")   