# extensions
from flask_wtf import FlaskForm
from wtforms import (
  TextField, PasswordField, BooleanField, SubmitField
)
from wtforms.validators import (
  DataRequired, Email, Length, Regexp, EqualTo
)
from wtforms import ValidationError

from ..models import User

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::

class LoginForm(FlaskForm):
  email = TextField('Email', 
      validators=[DataRequired(), Length(1, 64), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember me')
  submit = SubmitField('Log in')




class RegistrationForm(FlaskForm):
  username = TextField('Username', validators=[DataRequired('username'), Length(1, 64),
                                  Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
        'Usernames must have only latters numbers, dots or underscores')])
  
  email = TextField('Email', validators=[DataRequired('email'), Email(), Length(1, 64)])
  password = PasswordField('Password', validators=[DataRequired('password'), 
                        EqualTo('password2', message='Password must match.')])
  password2 = PasswordField('Confirm password', validators=[DataRequired('password2')])
  submit = SubmitField('Register')

  def validate_email(self, field):
    if User.query.filter_by(email=field.data).first():
      raise ValidationError('Email already registered.')

  def validate_username(self, field):
    if User.query.filter_by(username=field.data).first():
      raise ValidationError('Username already in use.')
  