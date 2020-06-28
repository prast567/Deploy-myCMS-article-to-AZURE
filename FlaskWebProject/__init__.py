"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
app.debug = True
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
handler.setFormatter(formatter)
app.logger.addHandler(handler)


Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
