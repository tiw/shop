# -*- coding: utf-8 -*-
from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash

__author__ = 'wangting'

from . import db
from flask_login import UserMixin
from . import login_manager


class System(db.Model):
    __tablename__ = 'systems'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    sub_systems = db.relationship("SubSystem", secondary='system_subsystem_link')

    def __repr__(self):
        return self.name


class SubSystem(db.Model):
    __tablename__ = 'sub_systems'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    system = relationship(System, secondary='system_subsystem_link')


class SystemSubSystemLink(db.Model):
    __tablename__ = 'system_subsystem_link'
    system_id = db.Column(db.Integer, db.ForeignKey('systems.id'), primary_key=True)
    subsystem_id = db.Column(db.Integer, db.ForeignKey('sub_systems.id', primary_key=True))


class SystemInterface(db.Model):
    __tablename__ = 'system_interfaces'
    id = db.Column(db.Integer, primary_key=True)
    src_system_id = db.Column(db.Integer, db.ForeignKey('systems.id'))
    target_system_id = db.Column(db.Integer, db.ForeignKey('systems.id'))
    src_system = relationship(System, foreign_keys=src_system_id)
    target_system = relationship(System, foreign_keys=target_system_id)

    function_description_id = db.Column(db.String(256))
    data_schema = db.Column(db.Text)
    data_sample = db.Column(db.Text)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True)
    email = db.Column(db.String(256), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    users = db.relationship('User', backref='role')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
