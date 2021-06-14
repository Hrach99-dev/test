from operator import le
import random
from flask import render_template, redirect, Blueprint, session, url_for
from myproject.game.forms import GameForm



games = Blueprint('games', __name__)


def get_content():
    with open('file.text') as txt:
        content = txt.readlines()
    return content

def replace_content(mlist):
    return [el.replace('\n', '') for el in mlist]


def split_quest_ans_list(random_quest_list):
    quest_ans_dict = {}
    for i in random_quest_list:
        ans_dict = {}
        key, value = i.split('-')
        ans_list = value.split(',')
        ans_dict['correct'] = ans_list[0]
        ans_dict['wrong1'] = ans_list[1]
        ans_dict['wrong2'] = ans_list[2]
        ans_dict['wrong3'] = ans_list[3]
        quest_ans_dict[key] = ans_dict
    return quest_ans_dict


mdict = {}
count = 0
content = get_content()
replaced_content = replace_content(content)
splited_quest_ans_list = split_quest_ans_list(replaced_content)
keys = list(splited_quest_ans_list.keys())
correct_result = 0


@games.route('/runner')
def runner():
    return render_template('game.html')


@games.route('/millionaire', methods=['GET', 'POST'])
def millionaire():

    global mdict
    global count
    global correct_result

    key = keys[count]
    value_dict = splited_quest_ans_list[f'{key}']
    value_list = list(value_dict.values())
    random.shuffle(value_list)
    form = GameForm()
    form_answer = form.global_answer.data
    if form.validate_on_submit():
        if count == len(keys) - 1:
            return redirect(url_for('games.dashboard'))

        if form_answer == value_dict['correct']:
            flag = True
            correct_result += 1 
        else:
            flag = False
            

        mdict[key] = [form_answer, flag]
        count += 1
                    
        return redirect(url_for('games.millionaire'))
    return render_template('millionaire.html', key=key, form=form, value_list=value_list, mdict=mdict, count=count, correct_result=correct_result)
    

@games.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')