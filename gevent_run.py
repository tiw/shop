# -*- coding: utf-8 -*-
__author__ = 'wangting'


from gevent.wsgi import WSGIServer
from app import create_app


http_server = WSGIServer(('', 5000), create_app('development'))
http_server.serve_forever()
