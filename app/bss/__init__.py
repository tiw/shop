# -*- coding: utf-8 -*-
__author__ = 'wangting'

from .. import db


class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Fruit(db.Model):
    __tablename__ = 'fruits'