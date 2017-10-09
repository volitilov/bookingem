#!venv/bin/python3.5

#!venv/bin/python3.5

import os

from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

from app.models import User
from app import create_app, db

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
  return dict(app=app, db=db, User=User)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
  '''Запускает модульные тесты'''
  import unittest, subprocess
  print('')
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)
  subprocess.call('rm data_test.sqlite', shell=True)

@manager.command
def clear_users():
  '''Удаляет всех пользователей из базы'''
  users = User.query.all()
  for user in users:
    db.session.delete(user)
  db.session.commit()
  print('All users delete')


# ::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
  manager.run()