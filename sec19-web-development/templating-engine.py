# Flask evaluates data within using Python expressions - {{ }}, even though this is specified in the index.html
# It uses, Jinja - a templating language 
# https://jinja.palletsprojects.com/en/2.11.x/

# Ex:

# <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">

# The above line in index.html will look for favicon.ico in the static folder

# url_for() is a method, part of flask - from flask import url_for



