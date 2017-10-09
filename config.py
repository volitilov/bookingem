import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)

  # включение / отключение CSRF
  CSRF_ENABLED = True

  # папка, где храняться файлы SQLAlchemy-migrate
  SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
  # отслеживет изменение объектов и испускает сигналы
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  APP_ADMIN = 'volitilov@gmail.com'

  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 465
  MAIL_USERNAME = 'volitilov@gmail.com'
  MAIL_PASSWORD = 'Kendar6709'
  MAIL_USE_SSL = True
  MAIL_DEFAULT_SENDER = MAIL_USERNAME


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class DevelopmentConfig(Config):
  # включение / отключение отладчика
  DEBUG = True

  # путь к файлу к базе данных.
  SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data_dev.sqlite')



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class TestingConfig(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data_test.sqlite')



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')




config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig,
  'production': ProductionConfig,

  'default': DevelopmentConfig
}