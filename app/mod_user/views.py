from flask import render_template,request,session,g,redirect,url_for
from flask_login import login_user,logout_user,login_required,current_user

from . import mod_user
from .forms import RegisterForm
from .models import User
from app import db

@mod_user.route('/register',methods=['GET','POST'])
def register():
	registerform = RegisterForm()
	
	if registerform.validate_on_submit():
		user = User(username=registerform.username.data,
					email=registerform.email.data,
					password=registerform.password.data
					)
		db.session.add(user)
		db.session.commit()

		return "successfully registered."

	return render_template('register.html',form=registerform)