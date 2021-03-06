from flask_restful import Resource
from .User import Users, users_list

from app import db
from models import User, Role

from . import parser
def user_exists(name):
    n = User.query.filter_by(user_name=name).count()
    if n:
        return True
    else:
        return False

class UserHandling(Resource):

    def post(self):
        args = parser.parse_args()
        if not user_exists(args['user_name']):
            db.session.add(User(**args))
            db.session.commit()
            return {"uid": user.user_id for user in users_list if user.user_name == args['user_name']}, 201
        else:
            return {"uid": user.user_id for user in users_list if user.user_name == args['user_name']}, 409

    def put(self):
        args = parser.parse_args()
        if not user_exists(args['user_name']):
            return {'message': 'user doesnt exist'}, 404
        else:
            for i in range(len(users_list)):
                if args['user_name'] == users_list[i].user_name:
                    for key, val in args.items():
                        users_list[i][key] = val
                    return {'name': users_list[i].user_name}, 200

    def delete(self):
        args = parser.parse_args()
        if not user_exists(args['user_name']):
            return {'message': 'user doesnt exist'}, 404
        else:
            for i in range(len(users_list)):
                if users_list[i].user_name == args['user_name']:
                    del users_list[i]
                    return 200

    def get(self):
        datalist = {}
        for i in range(len(users_list)):
            datalist[users_list[i].user_id] = [users_list[i].user_name, users_list[i].role_id]
        return datalist, 200


