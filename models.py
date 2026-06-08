from ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()

class User(db.Model, BaseModel, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), default="Guest")
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def set_password(self, password):
        self.password = generate_password_hash(password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class Championship(db.Model, BaseModel):
    __tablename__ = "championships"
    id = db.Column(db.Integer(), primary_key=True)
    sport = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    winner = db.Column(db.String(100), nullable=False)
    runner_up = db.Column(db.String(100), nullable=False)
    final_score = db.Column(db.String(50), nullable=False)
    team1 = db.Column(db.String(100), nullable=False)
    team2 = db.Column(db.String(100), nullable=False)
    semi_final_1 = db.Column(db.String(250), nullable=False)
    semi_final_2 = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    img = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=False)