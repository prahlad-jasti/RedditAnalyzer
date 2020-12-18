from flask import Flask, render_template, request
from pymongo import MongoClient
from StatsCalculator import RedditStatistics as redStat

app = Flask(__name__)
client = MongoClient('127.0.0.1', 27017)
db = client.pymongo_test
posts = db.posts


@app.route("/")
def home():
    title = "Statistics"
    return render_template("home.html", title=title)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        users = request.json
        posts.insert_one(users)
    return render_template("hello.html")


@app.route('/results')
def results():
    users = posts.find().sort([('_id', -1)]).limit(1).next()
    reddit_calc = redStat(users['user_1'], users['user_2'], users['time_zone']).merge()
    return render_template("results.html", stats=reddit_calc)


if __name__ == "__main__":
    app.run(debug=True)
