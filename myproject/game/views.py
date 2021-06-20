import random
from flask import render_template, redirect, Blueprint, session, url_for
from myproject.game.forms import GameForm
from flask_login import login_required, current_user
from myproject.models import User, GameQuest
from myproject import db

games = Blueprint('games', __name__)





mdict = {}
count = 0
correct_result = 0


@games.route('/runner')
@login_required
def runner():
    user = User.query.filter_by(id=current_user.id).first()
    user.point = 0
    db.session.commit()
    return render_template('game.html')


@games.route('/millionaire', methods=['GET', 'POST'])
@login_required
def millionaire():

    global mdict
    global count
    global correct_result

    quests = GameQuest.query.all()
    quest = quests[count]

    
    value_list = [quest.correct, quest.wrong1, quest.wrong2, quest.wrong3]
    random.shuffle(value_list)
    form = GameForm()
    form_answer = form.global_answer.data
    user = User.query.filter_by(id=current_user.id).first()
    
    if form.validate_on_submit():
        if count == len(quests) - 1:
            user.point = correct_result
            db.session.commit()
            return redirect(url_for('users.dashboard'))

        if form_answer == quest.correct:
            flag = True
            correct_result += 1 
        else:
            flag = False
            

        mdict[quest.quest] = [form_answer, flag]
        count += 1
                    
        return redirect(url_for('games.millionaire'))
    return render_template('millionaire.html', key=quest.quest, form=form, value_list=value_list, mdict=mdict, count=count, correct_result=correct_result)
    
