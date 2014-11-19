# -*- coding: utf-8 -*-

__author__ = 'wangting'

from flask import Blueprint
from .. import admin as admin_ext
from .. import db
from flask_admin.contrib.sqla import ModelView
from app.models import Product, Purchase, LineItem, User, Role, Vendor

admin = Blueprint('admin', __name__)
admin_ext.add_view(ModelView(Product, db.session))
admin_ext.add_view(ModelView(Purchase, db.session))
admin_ext.add_view(ModelView(LineItem, db.session))
admin_ext.add_view(ModelView(User, db.session))
admin_ext.add_view(ModelView(Role, db.session))
admin_ext.add_view(ModelView(Vendor, db.session))
