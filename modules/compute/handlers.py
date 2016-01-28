from tornado.gen import coroutine
from cloudGate.httpbase import HttpBaseHandler

class ComputeBaseHandler(HttpBaseHandler):
    #the ProcessorFac return the real processor.
    p = ComputeProcessorFac()

class ServerActionHandler(ComputeBaseHandler):
    def post(self, tenat_id, server_id):
        #call process_base functions
        action = "reboot"
        p.ServerAction(tenat_id, server_id, action)

