from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
lm = LoginManager(app)
lm.session_protection ='Strong'

from app.mod_user import mod_user as user_blueprint

app.register_blueprint(user_blueprint)