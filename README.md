##Framework
```
  +-------------------------------+
  |           Horizon             |
  +-------------------------------+
                 |
                 V
  +-------------------------------+
  |  cloudGate RESTFUL handlers   |
  +-------------------------------+
  |        origin APIs            |
  +-------------------------------+
      |            |
      V            V
  +--------+   +------+
  | aliyun |   |amazon|  ...             //processors
  +--------+   +------+
```
###Request Procedure：
Horizon send HTTP request to cloudGate, cloudGate handler process the request,
handler call origin APIs only，handler don't know the real processing is, 
origin APIs is abstract of bottom processing。
The advantage of this is: when expend to other platform, origin APIs and handlers needn't modify，
 just add processors. 
On the other hand, if user use amozon image and aliyun oss, we just edit some configure then can 
realize unify management. 

##Modules
```
▾ modules
  ▾ block_storage
    ▾ aliyun
        __init__.py
        processor.py                   //real processors
    ▸ amazon
      __init__.py
      api_factory.py                   //produce real processor
      handlers.py                      //handle Horizon request
      process_base.py                  //define interface of processor
      url.py                           //define REST urls
  ▸ clustering
  ▸ compute
  ▸ data_processing
  ▸ database_service
  ▸ identity
  ▸ image_service
  ▸ mould
  ▸ networking
  ▸ object_storage
  ▸ orchestration
  ▸ shared_file_systems
  ▸ telemetry
```
###Module switch
```
MODULES_SWITCH = {
    "identity": 1,
    "mould": 0,
    "block_storage":1,
    "clustering":1,
    "compute":0,
    "data_processing":1,
    "database_service":1,
    "image_service":1,
    "networking":1,
    "object_storage":1,
    "orchestration":1,
    "shared_file_systems":1,
    "telemetry":1,
}
```
cloudGate define a switch for all modules, if value is 0 cloudGate will not init that module.

##API version surpport
we can define different version handler in url.py, and config witch version is current. 
and support lower version api. 

##A sample develop example
###Control aliyun ECS reboot
####Horzion request API
TODO
####Add url in compute/url.py
TODO
####Add handler in compute/handlers.py
TODO
####Add base processor in compute/process_base.py
TODO
####Add processor in compute/aliyun/processor.py
TODO
####Edit factory in compute/api_factory.py
TODO
