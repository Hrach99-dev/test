from flask import flash, request, render_template, redirect, url_for, Blueprint
from myproject import db
from myproject.models import User
from myproject.users.forms import LoginForm, RegisterForm



users = Blueprint('users', __name__)


@users.route('/registration', methods=['GET','POST'])
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.name.data,
                    surname=form.surname.data,
                    login=form.login.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


@users.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(login=form.login.data).first()

        if user is None:
            return redirect(url_for('users.login'))
        
        if user.check_password(form.password.data) and user:
            

            next = request.args.get('next')

            if next == None or not next[0] == '/':
               next = url_for('games.game') 
            
            return redirect(next)
        
            
            
    return render_template('login.html', form=form)


