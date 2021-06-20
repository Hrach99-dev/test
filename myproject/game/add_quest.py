
from flask_restful import Resource, reqparse
from myproject.models import GameQuest
from flask import jsonify
from myproject import db


parser = reqparse.RequestParser()
parser.add_argument('quest', type=str, required=True)
parser.add_argument('correct', type=str, required=True)
parser.add_argument('wrong1', type=str, required=True)
parser.add_argument('wrong2', type=str, required=True)
parser.add_argument('wrong3', type=str, required=True)



class Quest(Resource):

    def get(self, quest_id):
        quest = GameQuest.query.filter_by(id=quest_id).first()
        if quest:
            return {quest.id:{
                        'quest':quest.quest,
                        'correct': quest.correct,
                        'wrong1': quest.wrong1,
                        'wrong2': quest.wrong2,
                        'wrong3': quest.wrong3
                        }
                    }
        else:
            return {'msg':'The question does not exist'}


    def delete(self, quest_id):
        quest = GameQuest.query.filter_by(id=quest_id).first()
        
        if quest:
            db.session.delete(quest)
            db.session.commit()
            return {'msg':'Question deleted'}
        else:
            return {'msg':'The question does not exist'}


    def put(self, quest_id):
        quest = GameQuest.query.filter_by(id=quest_id).first()
        if quest:
            args = parser.parse_args()
            quest.quest = args['quest']
            quest.correct = args['correct']
            quest.wrong1 = args['wrong1']
            quest.wrong2 = args['wrong2']
            quest.wrong3 = args['wrong3']
            db.session.commit()
            return {'msg':'Question updated'}
        else:
            return {'msg':'The question does not exist'}
   
class AddQuest(Resource):

     def post(self):
        args = parser.parse_args()
        quest = args['quest']
        correct = args['correct']
        wrong1 = args['wrong1']
        wrong2 = args['wrong2']
        wrong3 = args['wrong3']

        db_quest = GameQuest.query.filter_by(quest=quest).first()
        if db_quest is None:
            new_quest = GameQuest(quest=quest, correct=correct, wrong1=wrong1, wrong2=wrong2,wrong3=wrong3)
            db.session.add(new_quest)
            db.session.commit()
            return {'msg':'Question created'}
        else:
            return {'msg':'The question already exists'}



class AllQuest(Resource):
    def get(self):
        quest = GameQuest.query.all()
        return {el.id:{'quest':el.quest,'correct': el.correct,'wrong1': el.wrong1,'wrong2': el.wrong2,'wrong3': el.wrong3} for el in quest}