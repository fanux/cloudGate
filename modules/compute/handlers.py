from tornado.gen import coroutine
from cloudGate.httpbase import HttpBaseHandler

class ComputeBaseHandler(HttpBaseHandler):
    #the ProcessorFac return the real processor.
    p = ComputeProcessorFac()

    def get(self):
        #TODO
        pass

class ServersHandler(ComputeBaseHandler):
    def get(self, tenant_id):
        #TODO
        pass

    def post(self, tenant_id):
        #TODO
        pass

class ServersDetailHandler(ComputeBaseHandler):
    def get(self, tenant_id):
        pass

class ServerHandler(ComputeBaseHandler):
    def get(self, tenant_id, server_id):
        pass
    
    def put(self, tenant_id, server_id):
        pass

    def delete(self, tenant_id, server_id):
        pass

class ServerActionHandler(ComputeBaseHandler):
    def post(self, tenant_id, server_id):
        #call process_base functions
        action = "reboot"
        p.ServerAction(tenant_id, server_id, action)

