# -*- encoding: utf-8 -*-
from tornado.web import *

import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class IdentityBaseHandler(tornado.web.RequestHandler):
    def options(self):
        pass
    def get(self):
        pass
