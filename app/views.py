from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():

    # strings
    my_name = "Shane R Scott"

    # integers
    my_age = 42

    #lists
    langs = ["Python", "JavaScript", "Bash", "C", "Ruby"]

    # dictionaries
    friends = {
        "Tom": 30,
        "Amy": 60,
        "Tony": 56,
        "Clarissa": 23
    }

    # tuples
    colors = ("red", "green", "orange", "blue", "ultimateColor")

    # booleans
    cool = True

    # sample html bit, for escaping demo

    my_html = "<h1>SOME HTML</h1>"

    # classes
    class GitRemote:
        def __init__(self, name, desc, url, other):
            self.name = name
            self.desc = desc
            self.url = url
            self.other = other

        def pull(self):
            return f"pulling repo {self.name}"

        def clone(self):
            return f"cloning into {self.url}"

    my_remote = GitRemote (
        name="Flask Jinja",
        desc="template design tutorial",
        url="https://github.com/bamacanuck/jinjApp.git",
        other="otherVariable"
    )

    suspect = "<script>alert('HACKED')</script>"

    # functions
    def repeat(x, qty):
        return x * qty

        # family = {
    #     "Shawn": {
    #         age: 46,
    #         loc: "Idaho",
    #         kids:{
    #             "Saoirse", "Fianna"
    #         }
    #     },
    #     "Shannon": {
    #         age: 43,
    #         loc: "Japan",
    #         kids:{
    #             "Roland", "Reilly"
    #         }            
    #     },
    #     "Shane": {
    #         age: 42,
    #         loc: "Georgia",
    #         kids:{
    #             "Lil"
    #         }
    #     }
    # }

    
    return render_template("public/jinja.html", my_name=my_name, my_age=my_age,
    langs=langs, friends=friends, colors=colors, cool=cool,
    GitRemote=GitRemote, my_remote=my_remote, repeat=repeat, my_html=my_html, suspect=suspect)

@app.route("/x")
def redX():
    return "<h1 style='color : red'>X</h1>"