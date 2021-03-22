from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# flask instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"

# Form Class
class NameForm(FlaskForm):
    name = StringField("What is your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

    	## Fields
	# BooleanField
	# DateField
	# DateTimeField
	# DecimalField
	# FileField
	# HiddenField
	# MultipleField
	# FieldList
	# FloatField
	# FormField
	# IntegerField
	# PasswordField
	# RadioField
	# SelectField
	# SelectMultipleField
	# SubmitField
	# StringField
	# TextAreaField

	## Validators
	# DataRequired
	# Email
	# EqualTo
	# InputRequired
	# IPAddress
	# Length
	# MacAddress
	# NumberRange
	# Optional
	# Regexp
	# URL
	# UUID
	# AnyOf
	# NoneOf

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

# Name page
@app.route("/name", methods=["GET", "POST"])
def name():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template("name.html", name=name, form=form)

