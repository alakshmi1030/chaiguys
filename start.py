from flask import Flask
from flask import render_template
from flask import request
from flask.ext.mail import Mail
from flask.ext.mail import Message
import smtplib
import mimetypes
import os

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'arcsmtpserver@gmail.com'
MAIL_PASSWORD = 'cha1nsaw'

app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/services")
def services():
	return render_template("services.html")

@app.route("/servicesdone")
def servicedone():
	return render_template("servicesdone.html")

@app.route("/submitted", methods=['POST'])
def submitted():
	name = "Full Name: " + request.form["fullName"]
	email = "Email: " + request.form["emailAddress"]
	organization = "Organization: " + request.form["organization"]
	#preferredContact = "Preferred Contact: " + request.form["preferredContact"]
	phone = "Phone Number: " + request.form["phoneNumber"]
	extra = "Extra text: " + request.form["extraText"]

	everything = name + "\n" + email + "\n" + organization + "\n" + phone + "\n" + extra

	msg = Message('Catering request received - ' + email,sender="test@gmail.com",recipients=["calchaiguys@gmail.com"])
	msg.body = everything

	mail.send(msg)
	return render_template("servicesdone.html")

if __name__ == "__main__":
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)