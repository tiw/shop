# -*- coding: utf-8 -*-
__author__ = 'wangting'

from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_admin import Admin


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
admin = Admin()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(config_name)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)


    from main import main as main_blueprint
    from auth import auth as auth_blueprint
    from admin import admin as admin_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')

    import os.path
    _dir = os.path.dirname(os.path.abspath(__file__))
    app.template_folder = os.path.join(_dir, 'templates')

    return app