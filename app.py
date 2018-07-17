from flask import Flask
from flask_restful import Api

from resources.Role import Roles
from resources.Users import UserHandling
from resources.Login import UserAuth


app = Flask(__name__)
api = Api(app)

api.add_resource(UserAuth, '/login')
api.add_resource(UserHandling, '/user', endpoint='user')
api.add_resource(Roles, '/roles', endpoint='roles')


if __name__ == '__main__':
    app.run(debug=True)