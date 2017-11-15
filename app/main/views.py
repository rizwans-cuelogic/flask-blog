from flask import request,render_template,session,g,abort,redirect

from . import main

@main.route('/')
def index():
	return render_template('index.html')