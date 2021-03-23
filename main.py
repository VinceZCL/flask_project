from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# flask instance
app = Flask(__name__)
# SQLite database
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
# MySQL database
# "mysql://username:password@localhost/db_name"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1103@localhost/users"
# secret key
app.config["SECRET_KEY"] = "secret key"
# initialise database
db = SQLAlchemy(app)

## initialise db instruction

#$ winpty python
#>>> from main import db
#>>> db.create_all()

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), nullable=False)
	email = db.Column(db.String(120), nullable=False, unique=True)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)
	# create string
	def __repr__(self):
		return "<Name %r>" %self.name
# User Form Class
class UserForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	submit = SubmitField("Confirm")

# Form Class
class NameForm(FlaskForm):
    name = StringField("What is your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

    # Fields
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

    # Validators
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

# Filters      # {{ var|filters }}
# safe          # accept html tags
# capitalize
# lower
# upper
# title         # capitalize first alphabet from all words
# trim          # trim spaces
# striptags     # remove all html tags

@app.route('/user/add', methods=["GET", "POST"])
def add_user():
	name = None
	form = UserForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user is None:
			user = Users(name=form.name.data, email=form.email.data)
			db.session.add(user)
			db.session.commit()
		name = form.name.data
		form.name.data = ""
		form.email.data = ""
		flash("User added.")
	users = Users.query.order_by(Users.date_added)
	return render_template("add_user.html", form=form, name=name, users=users)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", username=name)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
	form = UserForm()
	name_to_update = Users.query.get_or_404(id)
	if request.method == "POST":
		name_to_update.name = request.form["name"]
		name_to_update.email = request.form["email"]
		try:
			db.session.commit()
			flash("User Updated.")
			return render_template("update.html", form=form, name_to_update=name_to_update)
		except:
			flash("There was a problem.")
			return render_template("update.html", form=form, name_to_update=name_to_update)
	else:
			return render_template("update.html", form=form, name_to_update=name_to_update)

# custom error

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
        flash("Form Submitted.")
    return render_template("name.html", name=name, form=form)
