from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client.pymongo_test
posts = db.posts

bills_post = posts.find_one({'user_1': 'sidewind864'})
print(bills_post)