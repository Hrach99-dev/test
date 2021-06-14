from myproject import db
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.security import safe_str_cmp


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)



class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    # point = db.Column(db.Integer, default=0)
    login = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    # token = db.Column(db.Text)

    def __init__(self, name, surname, login, password) -> None:
        self.name = name
        self.surname = surname
        self.login = login
        # self.token = token
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f'User - {self.name} {self.surname}'


# def authenticate(login, password):
#     user = User.query.filter_by(login=login).first()

#     if user and safe_str_cmp(user.password, password):
#         return user

# def identity(payload):
#     user_id = payload['identity']
#     return User.query.filter_by(id=user_id).first()