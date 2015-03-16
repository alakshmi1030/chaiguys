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


app.run()