#!/usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/highlights")
def hightlights_():
    return render_template("highlights.html")


@app.route("/")
def index():
    return render_template("homepage.html")


@app.route("/latest")
def latest():
    return render_template("latest.html")


@app.route("/menu")
def menu_():
    return render_template("menupage.html")


@app.route("/p")
def portfolio_():
    return render_template("Portfolio.html")





@app.route("/g")
def gallery():
    return render_template("profile.html")






'''
@app.route("/b",method=["GET", "POST"])
def index():
    return "Method use is %s" % request.method
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


