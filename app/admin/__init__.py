# -*- coding: utf-8 -*-
from app.models import SystemInterface, System

__author__ = 'wangting'

from flask import Blueprint
from .. import admin as admin_ext
from .. import db
from flask_admin.contrib.sqla import ModelView


admin = Blueprint('admin', __name__)
admin_ext.add_view(ModelView(System, db.session))
admin_ext.add_view(ModelView(SystemInterface, db.session))
