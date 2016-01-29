from tornado.gen import coroutine
from cloudGate.httpbase import HttpBaseHandler

class LowVersionBlockStorageBaseHandler(HttpBaseHandler):   
    def get(self):
        pass

class BlockStorageBaseHandler(HttpBaseHandler):
    #TODO init a processor
    def get(self):
        pass

class VolumesHandler(BlockStorageBaseHandler):
    def get(self, tenant_id):
        pass

    def post(self, tenant_id):
        pass

class VolumesDetailHandler(BlockStorageBaseHandler):
    def get(self):
        pass

class VolumeHandler(BlockStorageBaseHandler):
    def get(self, tenant_id, volume_id):
        pass

    def put(self, tenant_id, volume_id):
        pass

    def delete(self, tenant_id, volume_id):
        pass

class VolumeMetadataHandler(BlockStorageBaseHandler):
    def get(self, tenant_id, volume_id):
        pass

    def put(self, tenant_id, volume_id):
        pass

class VolumeActionHandler(BlockStorageBaseHandler):
    def post(self, tenant_id, volume_id):
        pass

class SnapshotsHandler(BlockStorageBaseHandler):
    def get(self, tenant_id):
        pass

    def post(self, tenant_id):
        pass

class SnapshotsDetailHandler(BlockStorageBaseHandler):
    def get(self, tenant_id):
        pass

class SnapshotHandler(BlockStorageBaseHandler):
    def get(self, tenant_id, snapshot_id):
        pass

    def delete(self, tenant_id, snapshot_id):
        pass

    def put(self, tenant_id, snapshot_id):
        pass

class SnapshotMetadataHandler(BlockStorageBaseHandler):
    def get(self, tenant_id, snapshot_id):
        pass

    def put(self, tenant_id, snapshot_id):
        pass
