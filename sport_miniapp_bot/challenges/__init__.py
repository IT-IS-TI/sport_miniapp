from pymongo.mongo_client import MongoClient
from config import url
import random
from take_hours import All_sport_sessions
from json import loads

client = MongoClient(url)
db = client['SportAchievements']


class Challenge:
    def __init__(self, name):
        self.model = "challenge"
        self.name = name
        self.short_description = ""
        self.full_description = ""
        self.xp = 0
        self.sp = 0
        All_sport_sessions['Full hours'] = 0
        self.goal = All_sport_sessions
        self.id = str(random.randint(1000, 9999))


collection_challenges = db['challenges']

def return_challenges():
    all_challenges = collection_challenges.find()
    lst = []
    for i in all_challenges:
        test = '\n' + '\n'.join(f'{k}: {v}' for k, v in i['goal'].items())
        lst.append(f"#{i['id']}\n Name: {i['name']}\n Short_description: {i['short_description']}\n Full_description: {i['full_description']}\n Xp: {i['xp']}\n Sp: {i['sp']}\n Goal:{test}\n")
    return lst

def return_one_challenge(id):
    test = '\n'.join(f'{k}: {v}'for k,v in collection_challenges.find_one({'id':id})['goal'].items())
    return f"#ID {collection_challenges.find_one({'id':id})['id']}\n"  \
           f"Name {collection_challenges.find_one({'id':id})['name']}\n" \
           f"Short_description: {collection_challenges.find_one({'id':id})['short_description']}\n" \
           f"Full_description: {collection_challenges.find_one({'id':id})['full_description']}\n" \
           f"Xp: {collection_challenges.find_one({'id':id})['xp']}\n" \
           f"Sp: {collection_challenges.find_one({'id':id})['sp']}\n" \
           f"Goal:{test}\n"