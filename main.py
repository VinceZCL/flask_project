from flask import Flask, render_template

# flask instance
app = Flask(__name__)

# route decorator
@app.route("/")
def index():
#     return "<h1>Hello World</h1>"
    txt = "pepe <strong>stronk</strong>"
    lst = ["abc", "xyz", 420, True]
    return render_template("index.html", txt=txt, lst=lst)

## Filters      # {{ var|filters }}
# safe          # accept html tags
# capitalize
# lower
# upper
# title         # capitalize first alphabet from all words
# trim          # trim spaces
# striptags     # remove all html tags

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", username=name)

## custom error

# invalid url
@app.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404

# server error
@app.errorhandler(500)
def serverDed(e):
    return render_template("500.html"), 500