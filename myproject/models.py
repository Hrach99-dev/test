from myproject import db, login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(64))
    point = db.Column(db.Integer)
    login = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))


    def __init__(self, name, surname, email, point, login, password) -> None:
        self.name = name
        self.surname = surname
        self.email = email
        self.point = point
        self.login = login
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f'User - {self.name} {self.surname}'
