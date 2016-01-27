# -*- coding:utf-8 -*-
from httpbase import *

MODULES_SWITCH = {
    "identity": 1,
    "test": 1,
}

URL_SETTINGS = []

if MODULES_SWITCH["identity"]:
    from cloudGate.modules.identity.url import identity_urls

    URL_SETTINGS = URL_SETTINGS + identity_urls

if MODULES_SWITCH["test"]:
    from cloudGate.modules.test.url import test_urls 

    URL_SETTINGS = URL_SETTINGS + test_urls
