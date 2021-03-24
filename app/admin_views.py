from app import app

@app.route("/admin/dashboard")
def adminDashboard():
    return "<h1>admin dashboard</h1>"

@app.route("/admin/profile")
def adminProfile():
    return "<h1>admin profile</h1>"

@app.route("/admin/x")
def adminX():
    return "<h1 style='color : red'>X</h1>"