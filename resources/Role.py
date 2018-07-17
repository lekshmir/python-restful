from flask_restful import Resource


class Role:
    def __init__(self, **kwargs):
        self.role_id = kwargs['role_id']
        self.role = kwargs['role']


class Roles(Resource):
    def get(self):
        return [role.__dict__ for role in roles_list], 200


roles_list = []
r = {'role_id': 1, 'role': 'admin'}
roles_list.append(Role(**r))
r = {'role_id': 2, 'role': 'end_user'}
roles_list.append(Role(**r))

