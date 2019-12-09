from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

login_manager = LoginManager(app)
# login_manager.init_app(app)
login_manager.login_view = 'signin'


def makeApp(test_config=None):
    appDB = Flask(__name__,instance_relative_config=True)
    appDB.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'Group12\'s-super-secret-key',
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    )
    if test_config is None:
        # reload the config if it exits but check for not exit
        appDB.config.from_pyfile("config.py",silent=True)
    else:
        appDB.config.update(test_config)

    try:
        os.makedirs(appDB.instance_path)
    except OSError:
        pass
    db.init_app(appDB)

    return app
        
from app import routes, models