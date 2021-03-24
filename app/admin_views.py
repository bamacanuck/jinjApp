from app import app

from flask import render_template

@app.route("/admin/dashboard")
def adminDashboard():
    return render_template("admin/dashboard.html")

@app.route("/admin/profile")
def adminProfile():
    return "<h1>admin profile</h1>"

@app.route("/admin/x")
def adminX():
    return "<h1 style='color : red'>X</h1>"