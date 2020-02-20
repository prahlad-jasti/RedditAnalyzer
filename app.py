from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import datetime
import json
from Bot import RedditStatistics as redStat
app = Flask(__name__)
client = MongoClient('127.0.0.1', 27017)
db = client.pymongo_test
posts = db.posts
@app.route("/")
def home():
    title = "Doge"
    return render_template("home.html", title=title)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        users = request.json
        result = posts.insert_one(users)
        print('One post: {0}'.format(result.inserted_id))
    return render_template("hello.html")

if __name__ == "__main__":
    app.run(debug=True)
