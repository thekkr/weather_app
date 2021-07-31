from flask import Flask,request,render_template,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager
import os

# login_manager = LoginManager()
app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = "Kkr@6362"
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///'+os.path.join(BASE_DIR,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# login_manager.init_app(app)



from weather_app.core.views import core



app.register_blueprint(core)
