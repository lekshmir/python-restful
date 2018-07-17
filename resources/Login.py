from flask_restful import Resource
from .Users import user_exists
from .User import users_list
import base64
from . import parser


class UserAuth(Resource):
    def get(self):
        args = parser.parse_args()
        if not user_exists(args['user_name']):
            return {'message': 'user doesnt exist'}, 404
        else:
            for item in users_list:
                if args['user_name'] == item.user_name:
                    pwd = base64.b64decode(item.password)
                    if pwd == args['password'].encode('utf-8'):
                        return {'name': item.user_name}, 200
                    else:
                        return {'message': 'incorrect password'}, 404
