import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_jwt import JWT, jwt_required, current_identity
# from myproject.models import authenticate, identity


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'msk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app, db)


# jwt = JWT(app, authenticate, identity)


from myproject.core.views import core
from myproject.users.views import users
from myproject.game.views import games


app.register_blueprint(users)
app.register_blueprint(core)
app.register_blueprint(games)