from flask import (
  render_template, redirect, url_for, flash, request,
  current_app
)
# extensions
from flask_login import (
  login_required, login_user, logout_user, current_user
)

from . import auth, User, send_email
from .. import db
from .forms import LoginForm, RegistrationForm

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::


@auth.route('/login', methods=['GET', 'POST'])
def login():
  title = 'Login'
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user, form.remember_me.data)
      return redirect(request.args.get('next') or url_for('main.index'))
  return render_template('auth/login.html', title=title, form=form)


@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))



@auth.route('/register', methods=['GET', 'POST'])
def register():
  app = current_app._get_current_object()
  title = 'Registration'
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User( email = form.email.data,
                 username = form.username.data,
                 password = form.password.data )
    db.session.add(user)
    db.session.commit()
    token = user.generate_confirmation_token()
    if app.config['APP_ADMIN']:
      send_email(app.config['APP_ADMIN'], 'New User', 'mail/new_user', user=user)
      send_email(form.email.data, 'Потверждение почты', 
                          'auth/email/confirm', token=token, user=user)
    return redirect(url_for('main.index'))
  return render_template('auth/register.html', title=title, form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
  if current_user.confirmed:
    return redirect(url_for('main.index'))
  if current_user.confirm(token):
    flash('Ваш аккаунт потверждён спосибо!')
  else:
    flash('Ваша ссылка не действительна либо истекло время ссылки.')
  return redirect(url_for('main.index'))
