from flask_wtf import Form
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length,EqualTo
from .models import User

class RegisterForm(Form):
	username = StringField('Username',validators=[DataRequired()]) 
	email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
	password = PasswordField('Password',validators=[DataRequired(),Length(1,64),EqualTo('confirm_password',message="Password must match.")])
	confirm_password =PasswordField('confirm_password',validators=[DataRequired()])
	submit = SubmitField("Register")


class LoginForm(Form):
	email = StringField('Email',validators=[ DataRequired(),Length(1,64),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	remember_me = BooleanField('remember_me',default=False)
	submit= SubmitField("Log In")
	