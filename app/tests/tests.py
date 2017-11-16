import os
import unittest
from flask import Flask
from .. import app,db
from ..mod_user.models import User,Blog
from flask_testing import TestCase
from ..mod_user.forms import LoginForm
class TestCase(unittest.TestCase):

	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
		self.app = app.test_client()
		db.create_all()
		
	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_all(self):
		rv = self.app.get('/login')
		print rv.status_code
		
	def test_adduser(self):
		user= User(username="test", email="test@test.com",password="as123456")
		db.session.add(user)
		db.session.commit()
		assert user in db.session

	def test_login_form(self):


	def test_login(self):
		user= User(username="test", email="test@test.com",password="as123456")
		db.session.add(user)
		db.session.commit()
		email="test@test.com"
		password="as123456"
		rv = self.app.post('/login', data=dict(
				email=email,
				password=password
			), follow_redirects=True)
		
		assert "You were logged in" in rv.data
		
if __name__ == '__main__':
	unittest.main()