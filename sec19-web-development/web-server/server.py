from flask import Flask
app = Flask(__name__)   # you use Flask class to instantiate an application called app
print(__name__)         # O/P: __main__ (Indicates this is the main file we are running)

@app.route('/')         # @ - denotes it's a decorator - app.route() decorator gives us some extra tools to build the web-server 
def hello_world():
    return 'Hello, Timon!'