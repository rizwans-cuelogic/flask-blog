from flask import render_template,request,session,g,redirect,url_for
from flask_login import login_user,logout_user,login_required,current_user

from . import mod_user
from .forms import RegisterForm
from .models import User,Blog


@mod_user.route('/register',methods=['GET','POST'])
def register():
	registerform = RegisterForm()
	
	if registerform.validate_on_submit():

		return render_template('register.html',form=registerform)

	return render_template('register.html',form=registerform)