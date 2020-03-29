from pymongo import MongoClient
from StatsCalculator import RedditStatistics as redStat
client = MongoClient('mongodb://localhost:27017')
db = client.pymongo_test
posts = db.posts

users = posts.find().sort([('_id', -1)]).limit(1).next()
reddit_calc = redStat(users['user_1'], users['user_2'])

print(reddit_calc.karma_2())