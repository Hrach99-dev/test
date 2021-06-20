import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager
from flask_restful import Api


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'msk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'dfg17653@gmail.com'
app.config['MAIL_PASSWORD'] = 'abcdfg123'
app.config['MAIL_DEFAULT_SENDER'] = 'dfg17653@gmail.com'



mail = Mail(app)

db = SQLAlchemy(app)
Migrate(app, db)


login_manager = LoginManager(app, db)

api = Api(app)


from myproject.game.add_quest import Quest, AllQuest, AddQuest



api.add_resource(Quest, '/quest/<quest_id>')
api.add_resource(AddQuest, '/addquest')
api.add_resource(AllQuest, '/allquest')


from myproject.core.views import core
from myproject.users.views import users
from myproject.game.views import games


app.register_blueprint(users)
app.register_blueprint(core)
app.register_blueprint(games)