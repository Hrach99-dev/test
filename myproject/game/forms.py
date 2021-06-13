from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class GameForm(FlaskForm):
    global_answer = StringField()
    submit = SubmitField('Check')