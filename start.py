from flask import Flask
from flask import render_template
from flask import request

app = Flask("start")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/services")
def services():
	return render_template("services.html")

@app.route("/submitted", methods=['POST'])
def submitted():
	name = "Full Name: " + request.form["fullName"]
	email = "Email: " + request.form["emailAddress"]
	organization = "Organization: " + request.form["organization"]
	#preferredContact = "Preferred Contact: " + request.form["preferredContact"]
	phone = "Phone Number: " + request.form["phoneNumber"]
	extra = "Extra text: " + request.form["extraText"]

app.run()