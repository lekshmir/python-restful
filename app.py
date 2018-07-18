from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
# from resources.Role import Roles



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sampledb.sqlite3'
api = Api(app)
db = SQLAlchemy(app)
# from resources.Users import UserHandling
# from resources.Login import UserAuth
# api.add_resource(UserAuth, '/login')
# api.add_resource(UserHandling, '/user', endpoint='user')
# api.add_resource(Roles, '/roles', endpoint='roles')


if __name__ == '__main__':
    import resources
    app.run(debug=True)