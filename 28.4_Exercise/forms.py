from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email, Length


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired('username cannot be blank'), Length(min=1, max=20)])
    password = PasswordField("Password", validators=[InputRequired('password cannot be blank'), Length(min=8, max=70)])
    email=StringField("Email", validators=[InputRequired('email cannot be blank'), Email(), Length(max=50)])
    first_name=StringField("First Name", validators=[InputRequired('first name cannot be blank'), Length(max=30)])
    last_name=StringField("Last Name", validators=[InputRequired('last namecannot be blank'), Length(max=30)])

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired('username cannot be blank')])
    password = PasswordField("Password", validators=[InputRequired('password cannot be blank')])    

class FeedbackForm(FlaskForm):
    title = StringField("Title", validators=[Length(min=1, max=100)])
    content=TextAreaField("Content", validators=[InputRequired('content cannot be blank')])
