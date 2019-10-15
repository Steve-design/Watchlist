from flask import Flask
from .config import DevConfig
app = Flask(__name__, instance_relative_config= True)
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
from app import views
from flask_bootstrap import Bootstrap
from app import views
from app import error

# Initializing Flask Extensions
bootstrap = Bootstrap(app)