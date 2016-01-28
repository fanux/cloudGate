from handlers import *

urls_v2_1 = [
    (r"/v2.1/(.*)/servers/(.*)/action", ServerActionHandler),
]

#if we support other version api, use urls = urls_v2_1 + urls_other_version
urls = urls_v2_1
