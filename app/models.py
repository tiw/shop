# -*- coding: utf-8 -*-
from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash

__author__ = 'wangting'

from . import db
from flask_login import UserMixin
from . import login_manager


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


class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    sku = db.Column(db.String(255))
    line_items = db.relationship('LineItem', backref=('product'))

    def __repr__(self):
        return self.name


class LineItem(db.Model):
    __tablename__ = 'lineitems'

    id = db.Column(db.Integer, primary_key=True)
    # @todo: unsigned
    total_price = db.Column(db.Integer)
    item_price = db.Column(db.Integer)
    # @todo: unsigned
    quantity = db.Column(db.Integer)
    gram = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchases.id'))


class Purchase(db.Model):
    __tablename__ = 'purchases'

    id = db.Column(db.Integer, primary_key=True)
    operator = db.Column(db.Integer, db.ForeignKey('users.id'))
    datetime = db.Column(db.DateTime)
    line_items = db.relationship('LineItem', backref='purchase')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
