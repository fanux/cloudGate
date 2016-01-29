from tornado.gen import coroutine
from cloudGate.httpbase import HttpBaseHandler

class NetworkingBaseHandler(HttpBaseHandler):   
    #TODO init a processor
    def get(self):
        pass

class NetworksHandler(NetworkingBaseHandler):
    def get(self):
        pass

    def post(self):
        pass

class NetworkHandler(NetworkingBaseHandler):
    def get(self, network_id):
        pass

    def put(self, network_id):
        pass

    def delete(self, network_id):
        pass

class SubnetsHandler(NetworkingBaseHandler):
    def get(self):
        pass

    def post(self):
        pass

class SubnetHandler(NetworkingBaseHandler):
    def get(self, subnet_id):
        pass

    def put(self, subnet_id):
        pass

    def delete(self, subnet_id):
        pass

class PortsHandler(NetworkingBaseHandler):
    def get(self):
        pass

    def post(self):
        pass

class PortHandler(NetworkingBaseHandler):
    def get(self, port_id):
        pass

    def put(self, port_id):
        pass

    def delete(self, port_id):
        pass
