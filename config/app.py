from flask import Flask
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from logging import getLogger
from flask_orator import Orator

from .database import config_by_name
from .email import Email
# from .uploads import Upload

db = Orator()
flask_bcrypt = Bcrypt()
logger = getLogger()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    # mail = Mail(app)
    app.config.from_object(config_by_name[config_name])
    app.config.from_object(Email)
    # app.config.from_object(Upload)

    db.init_app(app)
    mail.init_app(app)
    flask_bcrypt.init_app(app)

    return app

