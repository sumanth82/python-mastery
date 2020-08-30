import flask

from flask import url_for, Flask, render_template
app=Flask(__name__)

@app.route('/')

def my_home():
    return render_template('index.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/about.html')
def about_us():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/components.html')
def component():
    return render_template('components.html')

