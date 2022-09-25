from flask import Flask
from markupsafe import escape
from flask import render_template;

app = Flask(__name__)

#using jinja template
@app.route('/')
@app.route('/home/')
def homepage():
    return render_template('extend.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')