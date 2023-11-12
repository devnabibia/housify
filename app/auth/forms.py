from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):

    email = StringField('Your Email Address', validators=[Email(), DataRequired()])
    username = StringField('Enter your username', validators=[DataRequired()])
    contact = StringField('Enter your contact', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class UpdateProfileForm(FlaskForm):

    profile_pic = FileField('Profile Picture', validators=[])
    bio = TextAreaField('Bio')
    email = StringField('Your Email Address', validators=[Email(), DataRequired()])
    username = StringField('Enter your username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
            if User.query.filter_by(email=email.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('That username is taken')
