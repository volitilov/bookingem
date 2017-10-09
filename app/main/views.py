from flask import (
  render_template, url_for, redirect, request
)
# extensions
from flask_login import (
  current_user, login_user
)

from . import main, User
from .. import db
from ..auth.forms import LoginForm

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::

@main.route('/', methods=['GET', 'POST'])
def index():
  title = 'Home'
  return render_template('index.html', title=title)


@main.route('/admin', methods=['GET', 'POST'])
def login():
  title = 'Admin'
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user, form.remember_me.data)
      return render_template('admin.html')
  return render_template('auth/login.html', title=title, form=form)


@main.route('/books')
def books():
  title = 'Books'



@main.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@main.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'), 500
