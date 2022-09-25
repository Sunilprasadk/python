from flask import Flask
from markupsafe import escape
from flask import render_template;
from flask import url_for

app = Flask(__name__)

#variable rules
@app.route('/user/<username>')
def show_user_profile(username):
    # print whatever in the username
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # print only the integer
    return f'Post {post_id}'

@app.route('/post/<float:post_id>')
def show_subpath(post_id):
    # print only the floating number
    return f'Subpath {escape(post_id)}'

#unique urls
@app.route('/slashinboth/')
def show_user_both():
    # print this even we enter user or user/
    return "<p>I am a User! with or without /, I will print.</p>"

@app.route('/noslashboth')
def show_user_one():
    # produce 404 error when / mentioned
    return "<p>I am a User! With /, I will produce error</p>"


#render basic html template
@app.route("/")
@app.route("/home")
def hello_default():
    return render_template("home.html")

#passing values to template
@app.route("/about")
def hello_name():
    name="Sunil Prasad"
    return render_template('homewithname.html', name=name)