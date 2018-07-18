from flask_restful import reqparse


from .Users import UserHandling
from .Login import UserAuth
from .Role import Roles
from app import api
api.add_resource(UserAuth, '/login')
api.add_resource(UserHandling, '/user')
api.add_resource(Roles, '/roles')
parser = reqparse.RequestParser()
parser.add_argument('user_name', type=str, help='user name is a mandatory field', required=True)
parser.add_argument('password', type=str, help='Password needed for authentication', required=True)
parser.add_argument('user_id', type=str)
parser.add_argument('role_id', type=str)


