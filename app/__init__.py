from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
# breakpoint();
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'

from app import routes, models