from pymongo.mongo_client import MongoClient
from config import url
from user import collection_users

client = MongoClient(url)
db = client['SportAchievements']
collection_challenges = db['challenges']

#collection_challenges.insert_one(
#    {"id": 1234, "name": "Basketball", "points": 30, "short_description": "asdb", "full_description": "dasdqwe",
#     "xp": 10, "sp": 16, "goal": "gg"})
#
#collection_challenges.insert_one(
#    {"id": 4321, "name": "Football", "points": 15, "short_description": "qwe", "full_description": "vxcv",
#     "xp": 4, "sp": 2, "goal": "543"})



#collection_challenges.delete_one({"id":1234})
#collection_challenges.delete_one({"id":4321})
#collection_challenges.delete_one({"name":"Basketball"})
#collection_challenges.delete_one({"name":"Football"})

#x = collection_challenges.find()
#for i in x:
#   # collection_challenges.delete_one({"id": i["id"]})
#   print(i)


#collection_challenges.delete_one({"id":2968})
#collection_challenges.delete_one({"id":3272})
#

collection_challenges.delete_one({"id":'7340'})
collection_challenges.delete_one({"id":"3813"})
collection_challenges.delete_one({"id":"3794"})
collection_challenges.delete_one({"id":"4351"})
collection_challenges.delete_one({"id":"6512"})
collection_challenges.delete_one({"id":"2836"})
collection_challenges.delete_one({"id":"3986"})
collection_challenges.delete_one({"id":"5508"})






x = collection_challenges.find()

for i in x:
   # collection_challenges.delete_one({"id": i["id"]})
   print(i)



# for i in x:
#    print(i['id'], i['name'], i['points'], i['gemes'])


#print(collection_challenges.find_one({"id":4756}))