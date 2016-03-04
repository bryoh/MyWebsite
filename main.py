from flask import Flask, render_template

app = Flask(__name__)


@app.route("/about")
def portfolio_():
    return render_template("about.html")


@app.route("/highlights")
def portfolio_():
    return render_template("highlights.html")


@app.route("/")
def index():
    return render_template("homepage.html")


@app.route("/latest")
def index():
    return render_template("latest.html")


@app.route("/menu")
def portfolio_():
    return render_template("menupage.html")


@app.route("/portfolio")
def portfolio_():
    return render_template("Portfolio.html")





@app.route("/gallery")
def portfolio_():
    return render_template("Portfolio.html")






'''
@app.route("/b",method=["GET", "POST"])
def index():
    return "Method use is %s" % request.method
'''

if __name__ == "__main__":
    app.run()


