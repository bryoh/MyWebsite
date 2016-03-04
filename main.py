from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("profile.html")

'''
@app.route("/b",method=["GET", "POST"])
def index():
    return "Method use is %s" % request.method
'''

if __name__ == "__main__":
    app.run()


