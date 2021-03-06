# -*- coding: utf-8 -*-
__author__ = 'wangting'

from app import create_app
from os import getenv

app = create_app(getenv('FLASK_CONFIG') or 'production')

if __name__ == '__main__':
    app.run()
