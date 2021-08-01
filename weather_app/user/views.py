from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import login_required,login_user,logout_user,current_user
from weather_app import app,db
from weather_app.models import User
from weather_app.user.forms import LoginForm,RegistrationForm,UpdateForm
import os

users = Blueprint('users',__name__)
ALLOWED_EXTENSIONS = ['png','jpg','jpeg']

def allowed_file(filename):
    return '.' in filename and filename.split('.',1)[1] in ALLOWED_EXTENSIONS
#Logout

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))

#Login
@users.route('/login',methods=['POST','GET'])
def login():
     form = LoginForm()

     if form.validate_on_submit():

         user = User.query.filter_by(email = form.email.data).first()

         if user.check_password(form.password.data) and user is not None:

             login_user(user)

             next = request.args.get('next')

             if next==None or not next[0] == '/':
                 next = url_for('core.index')

             return redirect(next)

     return render_template('login.html',form=form)

#register
@users.route('/register',methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)


#update
@users.route('/account',methods=['GET','POST'])
def account():

    form = UpdateForm()

    if form.validate_on_submit():

        picture = request.files['picture']

        if picture and allowed_file(picture.filename):
            filename =  str(current_user.username)+ '.' + picture.filename.split('.',1)[1]
            picture.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            pic = filename
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_image = url_for('static',filename='profile_images/'+current_user.profile_image)
    return render_template('account.html',profile_image=profile_image,form=form)
