from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client.pymongo_test
posts = db.posts

for doc in posts.find():
    print (doc)