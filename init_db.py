from ext import app, db
from models import Championship, User

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(username="admin", role="Admin")
    admin.set_password("adminpass")
    admin.create()
