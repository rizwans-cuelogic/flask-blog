from flask import render_template,request,session,g,redirect,url_for,flash
from flask_login import login_user,logout_user,login_required,current_user
from app.main import main
from app.mod_user.models import User,Blog
from app import db
from . import mod_blog
from .forms import BlogForm


@mod_blog.route('/addblog')
@login_required
def add_blog():
	blogform = BlogForm()

	if blogform.validate_on_submit():
		if blogform.publication_date.data:
			blog = Blog(title=blogform.title.data,content=blogform.content.data,publication_date=blogform.publication_date.data)
		else:
			blog = Blog(title=blogform.title.data,content=blogform.content.data)
			
	return render_template('addblog.html',form=blogform) 

