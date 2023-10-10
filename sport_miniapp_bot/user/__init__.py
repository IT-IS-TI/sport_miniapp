from pymongo.mongo_client import MongoClient
from config import url
from challenges import collection_challenges

client = MongoClient(url)
db = client['SportAchievements']



class User:
    def __init__(self, id, state='start'):
        self.state = state
        self.id = id
        self.login = ''
        self.password = ''
        self.notifications = 'Off'
        self.Xp = 0
        self.Sp = 0
        x = collection_challenges.find()
        challenge = {}
        for i in x:
           challenge[str(i['id'])] = False
        self.challenge = challenge


collection_users = db['users']
collection_admin = db['admins']


