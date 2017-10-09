from flask import Flask

# extensions
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flaskext.lesscss import lesscss

from config import config

# ::::::::::::::::::::::::::::::::::::::::::::::::::

db = SQLAlchemy()
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
# при данном значении Flask-Login будет следить за IP-адресом 
# клиента и агентом браузера и завершать сеанс принудительно 
# при обнаружении изменений

login_manager.login_view = 'auth.login'
# присваиваится имя канечной точки, соответствующей станице 
# аутентификации. Так ка маршрут login находится внутри 
# макета в его начало добавленно имя макета

# ::::::::::::::::::::::::::::::::::::::::::::::::::

def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config[config_name])

  db.init_app(app)
  mail.init_app(app)
  login_manager.init_app(app)
  lesscss(app)

  from .main import main
  app.register_blueprint(main)
  from .auth import auth
  app.register_blueprint(auth)

  return app
