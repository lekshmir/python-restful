from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument('user_name', type=str, help='user name is a mandatory field', required=True)
parser.add_argument('password', type=str, help='Password needed for authentication', required=True)
parser.add_argument('user_id', type=str)
parser.add_argument('role_id', type=str)