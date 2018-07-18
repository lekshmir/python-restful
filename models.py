from app import db
import base64


class User(db.Model):
    user_id = db.Column('user_id', db.Integer, primary_key=True)
    user_name = db.Column('user_name', db.String(100))
    password = db.Column('password', db.String(100))
    role_id = db.Column('role_id', db.Integer, db.ForeignKey('role.role_id'))

    def __init__(self, **kwargs):
        # self.user_id = User.uid
        self.user_name = kwargs['user_name']
        self.password = base64.b64encode(kwargs['password'].encode('utf-8'))
        self.role_id = kwargs['role_id']


class Role(db.Model):

    role_id = db.Column('role_id', db.Integer, primary_key=True)
    role = db.Column('role', db.String(100))

    def __init__(self, **kwargs):
        self.role_id = kwargs['role_id']
        self.role = kwargs['role']