from app import db
import models


db.create_all()


r = {'role_id': 1, 'role': 'admin'}
db.session.add(models.Role(**r))
r = {'role_id': 2, 'role': 'end_user'}
db.session.add(models.Role(**r))
db.session.commit()

t = {'user_name': 'Lekshmi', 'password': 'lechu', 'role_id': 1}
db.session.add(models.User(**t))
t = {'user_name': 'Niveditha', 'password': 'nivi', 'role_id': 1}
db.session.add(models.User(**t))
db.session.commit()