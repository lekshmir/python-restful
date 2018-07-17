from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse
import base64



app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('user_name', type=str, help='user name is a mandatory field', required=True)
parser.add_argument('password', type=str, help='Password needed for authentication', required=True)
parser.add_argument('user_id', type=str)
parser.add_argument('role_id', type=str)

print(parser)


class User:
    uid = 1

    def __init__(self, **kwargs):
        self.user_id = User.uid
        self.user_name = kwargs['user_name']
        self.password = base64.b64encode(kwargs['password'].encode('utf-8'))
        self.role_id = kwargs['role_id']
        User.uid = User.uid + 1


class Roles:
    def __init__(self, **kwargs):
        self.role_id = kwargs['role_id']
        self.role = kwargs['role']


users_list = []
roles_list = []

t = {'user_name': 'Lekshmi', 'password': 'lechu', 'role_id': 1}
users_list.append(User(**t))
t = {'user_name': 'Niveditha', 'password': 'nivi', 'role_id': 1}
users_list.append(User(**t))
t = {'user_name': 'Akash', 'password': 'lechu', 'role_id': 2}
users_list.append(User(**t))


r = {'role_id': 1, 'role': 'admin'}
roles_list.append(Roles(**r))
r = {'role_id': 2, 'role': 'end_user'}
roles_list.append(Roles(**r))


def user_exists(name):
    name_list = [user.user_name for user in users_list]
    if name in name_list:
        return True
    else:
        return False


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


class UserHandling(Resource):
    def post(self):
        args = parser.parse_args()
        if not user_exists(args['user_name']):
            users_list.append(User(**args))
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


api.add_resource(UserAuth, '/login')
api.add_resource(UserHandling, '/user')


if __name__ == '__main__':
    app.run(debug=True)