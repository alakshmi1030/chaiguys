from flask import Flask
from flask import render_template
from flask import request

app = Flask("start")

@app.route("/")
def index():
	return render_template("index.html")


app.run()