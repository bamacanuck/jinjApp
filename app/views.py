from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():
    return render_template("public/jinja.html")

@app.route("/x")
def redX():
    return "<h1 style='color : red'>X</h1>"