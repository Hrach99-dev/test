from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from wtforms import ValidationError
from myproject.models import User

class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    

    def check_login(self,field):
        if User.query.filter_by(login=field.data).first():
            raise ValidationError('Your login has been registered!')



class VerificationForm(FlaskForm):
    verification_field1 = StringField('Verification code field 1', validators=[DataRequired()])
    verification_field2 = StringField('Verification code field 2', validators=[DataRequired()])
    verification_field3 = StringField('Verification code field 3', validators=[DataRequired()])
    verification_field4 = StringField('Verification code field 4', validators=[DataRequired()])
    verification_field5 = StringField('Verification code field 5', validators=[DataRequired()])
    verification_field6 = StringField('Verification code field 6', validators=[DataRequired()])
    submit = SubmitField('Verification')
