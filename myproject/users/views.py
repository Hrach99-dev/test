from random import randint
from flask import flash, request, render_template, redirect, url_for, Blueprint
from flask.globals import session
from myproject import db, mail
from myproject.models import User
from myproject.users.forms import LoginForm, RegisterForm, VerificationForm
from flask_mail import Message


users = Blueprint('users', __name__)


def generate_verification_code():
    verification_code = ''
    for _ in range(6):
        value = randint(0, 9)
        verification_code += str(value)

    return verification_code

@users.route('/registration', methods=['GET','POST'])
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        verification_code = generate_verification_code()
        msg = Message(f'{verification_code} is your verification code', recipients=[form.email.data])
        mail.send(msg)

        session['name'] = form.name.data
        session['surname'] = form.surname.data
        session['email'] = form.email.data
        session['login'] = form.login.data
        session['password'] = form.password.data
        session['verification_code'] = verification_code
        
        return redirect(url_for('users.verification'))

    return render_template('register.html', form=form)


  


@users.route('/verification', methods=['GET','POST'])

def verification():
    form = VerificationForm()

    if form.validate_on_submit():
        if '{}{}{}{}{}{}'.format(form.verification_field1.data,
            form.verification_field2.data,form.verification_field3.data,
            form.verification_field4.data,form.verification_field5.data,
            form.verification_field6.data) == session['verification_code']:
            user = User(name=session['name'],
                        surname=session['surname'],
                        email=session['email'],
                        point=0,
                        login=session['login'],
                        password=session['password'])

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('games.runner'))
        else:
            return redirect(url_for('users.register'))
    return render_template('verification.html', form=form)

@users.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(login=form.login.data).first()

        if user is None:
            return redirect(url_for('users.register'))
        
        if user.check_password(form.password.data) and user:
            

            next = request.args.get('next')

            if next == None or not next[0] == '/':
               next = url_for('games.runner') 
            
            return redirect(next)
        
            
            
    return render_template('login.html', form=form)


@users.route('/dashboard')
def dashboard():
    user = User.query.all()
    return render_template('dashboard.html', user=user)


