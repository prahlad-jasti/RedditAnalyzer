from flask import Flask, render_template, jsonify, request, make_response
import json
app = Flask(__name__)


@app.route("/")
def home():
    title = "Pornhub"
    return render_template("home.html", title = title)

@app.route('/hello', methods = ['GET','POST'])
def hello():
    if request.method == 'POST':
        asd = request.json
        print(asd["user_1"])
        print(asd["user_2"])
    return render_template("hello.html")
if __name__ == "__main__":
    app.run(debug=True)
