import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


app.config['SECRET_KEY'] = "Kkr@6362"
app.config['SQLCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(BASE_DIR+"data.sqlite")
app.config['SQLALCHMEY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)



login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'



## BluePrints
