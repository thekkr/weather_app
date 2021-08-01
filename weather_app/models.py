from weather_app import login_manager,db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model,UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128),index=True,unique=True)
    email = db.Column(db.String(128),index=True,unique=True)
    profile_image = db.Column(db.String(128),nullable=False,default="defaut_profile.png")
    password_hash= db.Column(db.String(128))

    def __init__(self,username,email,password):

        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)


    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username : {self.username}"
