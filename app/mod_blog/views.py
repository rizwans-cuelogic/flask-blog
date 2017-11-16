from flask import render_template,request,session,g,redirect,url_for,flash
from flask_login import login_user,logout_user,login_required,current_user
from app.main import main
from app.mod_user.models import User,Blog
from app import db
from . import mod_blog
from .forms import BlogForm


@mod_blog.route('/addblog',methods=['GET','POST'])
@login_required
def add_blog():
	blogform = BlogForm()

	if blogform.validate_on_submit():
		if blogform.publication_date.data:
			blog = Blog(title=blogform.title.data,
						content=blogform.content.data,
						publication_date=blogform.publication_date.data,
						author=current_user)
		else:
			blog = Blog(title=blogform.title.data,
						content=blogform.content.data,
						author=current_user)


		db.session.add(blog)
		db.session.commit()
		flash('Added blog successfully')
		return redirect(url_for('main.index'))	
			
	return render_template('addblog.html',form=blogform) 

@mod_blog.route('/listblog')
@login_required
def list_blog():

	blogs = current_user.blogs
	return render_template('listblog.html',blogs=blogs)

@mod_blog.route('/deleteblog/<int:id>')
@login_required	
def delete_blog(id):
	blog=Blog.query.filter_by(id=id).first()
	if blog:
		db.session.delete(blog)
		db.session.commit()
		return redirect(url_for('.list_blog'))

