from flask_wtf import FlaskForm
from ..models import User
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email,Regexp,EqualTo

class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),Email()])
    username = StringField('Username', validators=[DataRequired(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'Username have only letter no special carater')])
    password = PasswordField('Password',validators=[DataRequired(), EqualTo('password2',message='password much match.')])
    password2 = PasswordField('Confirm password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self,field):
         if User.query.filter_by(email=filter.data).first():
             raise ValidationError("email alredy register")

    def validate_username(self,field):
        if User.query.filter_by(username=field.data):
            raise ValidationError('user already using')
