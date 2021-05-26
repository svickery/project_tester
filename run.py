import os
from flask import Flask, render_template, url_for
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reviews")
def reviews():
    return render_template("reviews.html")


@app.route("/current")
def current():
    return render_template("current.html")


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True)
