from flask import Flask
from markupsafe import escape

app = Flask(__name__)

#default code
@app.route("/")
def hello_default():
    return "<p>Hello, World! I am learning <i>Flask</i></p>"

#route-1
@app.route("/home")
def hello_home():
    return "<p>Hey, This is <b>Home Route</b></p>"

#route-2
@app.route("/about")
def aboutpage():
    return "<p>Hai, I am <i>About Route</i></p>"


#this is normally through formatted string
@app.route("/about/<name>")
def getnamebyfu(name):
    return f"<p>Hai, I am {name}. Output this through the normal formatted string.</p>"

#html escaping - this prevents the injecting harm text, links and so-on
@app.route("/<name>")
def getnamebyes(name):
    return f"<p>Hai, I am {escape(name)}. Output this through the escape method.</p>"

#more than one route for a page
@app.route("/house")
@app.route("/heaven")
def samepages():
    return "<p>I am in Heaven refered to my home...!</p>"
