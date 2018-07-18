import base64


class Users:
    uid = 1

    def __init__(self, **kwargs):
        self.user_id = Users.uid
        self.user_name = kwargs['user_name']
        self.password = base64.b64encode(kwargs['password'].encode('utf-8'))
        self.role_id = kwargs['role_id']
        Users.uid = Users.uid + 1


users_list = []
t = {'user_name': 'Lekshmi', 'password': 'lechu', 'role_id': 1}
users_list.append(Users(**t))
t = {'user_name': 'Niveditha', 'password': 'nivi', 'role_id': 1}
users_list.append(Users(**t))
t = {'user_name': 'Akash', 'password': 'lechu', 'role_id': 2}
users_list.append(Users(**t))
