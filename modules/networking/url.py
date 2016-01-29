from handlers import *

urls = [
    (NETWORKING_BASE_URL, NetworkingBaseHandler),
    (NETWORKING_BASE_URL + "/v2/networks", NetworksHandler),
    (NETWORKING_BASE_URL + "/v2/networks/(.*)", NetworkHandler),

    (NETWORKING_BASE_URL + "/v2.0/subnets", SubnetsHandler),
    (NETWORKING_BASE_URL + "/v2.0/subnet", SubnetHandler),

    (NETWORKING_BASE_URL + "/v2.0/ports", PortsHandler),
    (NETWORKING_BASE_URL + "/v2.0/ports/(.*)", PortHandler), 
]

