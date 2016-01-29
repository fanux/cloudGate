# -*- encoding: utf-8 -*-
from cloudGate.httpbase import HttpBaseHandler

import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class IdentityBaseHandler(HttpBaseHandler):
    #TODO init a processor
    def get(self):
        pass

class UsersHandler(IdentityBaseHandler):
    def get(self):
        pass

    def post(self):
        pass

class UserHandler(IdentityBaseHandler):
    def get(self, user_id):
        pass

    def patch(self, user_id):
        pass

    def delete(self, user_id):
        pass

class UserPasswordHandler(IdentityBaseHandler):
    def post(self, user_id):
        pass

class UserGroupsHandler(IdentityBaseHandler):
    def get(self, user_id):
        pass

class RolesHandler(IdentityBaseHandler):
    def get(self):
        pass

    def post(self):
        pass

class RoleHandler(IdentityBaseHandler):
    def get(self, role_id):
        pass

    def patch(self, role_id):
        pass

    def delete(self, role_id):
        pass

class GroupsHandler(IdentityBaseHandler):
    def get(self):
        pass

    def post(self):
        pass

class GroupHandler(IdentityBaseHandler):
    def get(self, group_id):
        pass

    def patch(self, group_id):
        pass

    def delete(self, group_id):
        pass

class GroupUsersHandler(IdentityBaseHandler):
    def get(self, group_id):
        pass

class GroupUserHandler(IdentityBaseHandler):
    def put(self, group_id, user_id):
        pass

    def head(self, group_id, user_id):
        pass

    def delete(self, group_id, user_id):
        pass

class PoliciesHandler(IdentityBaseHandler):
    def get(self):
        pass

    def post(self):
        pass

class PolicyHandler(IdentityBaseHandler):
    def get(self, policy_id):
        pass

    def patch(self, policy_id):
        pass

    def delete(self, policy_id):
        pass
