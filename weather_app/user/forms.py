from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo
from weather_app.models import User
from flask_login import current_user
from flask_wtf.file import FileField

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):

    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Password must match')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self,username):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email already registred')

    def validate_username(self,username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username not available')

class UpdateForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    picture = FileField('Update Profile Picture')
    submit = SubmitField()

    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = self.email.data).first():
                raise ValidationError('Email already registered')

    def validate_username(self,username):
        if username.data!=current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError('Username already exists')
