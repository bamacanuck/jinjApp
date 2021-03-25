from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():

    my_name = "SRS"

    return render_template("public/jinja.html", my_name=my_name)

@app.route("/x")
def redX():
    return "<h1 style='color : red'>X</h1>"