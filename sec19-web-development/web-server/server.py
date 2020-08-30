from flask import Flask, render_template

app = Flask(__name__)   # you use Flask class to instantiate an application called app
print(__name__)         # O/P: __main__ (Indicates this is the main file we are running)

#@app.route('/')         # @ - denotes it's a decorator - app.route() decorator gives us some extra tools to build the web-server 
#def hello_world():
#    return 'Hello, Timon!'

# If you instead want to render the template from index.html use the below:

#@app.route('/')    # To render a template i.e an index.html file, flask always looks for a templates folder 
#def index(name=None):
#    return render_template('index.html', name=name)

@app.route('/<username>/<int:post_id>')           # You pass the <username> var value fetched from the website user to the function which calls index.hmtl

def index(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

                                    # After this add {{ name }} in index.html and run http://127.0.0.1:5000/Andrei: 
@app.route('/about.html')
def about_us():
    return render_template('about.html')

@app.route('/blog')     # This allows to access the web-page at: http://127.0.0.1:5000/blog
def blog():
    return 'Timon blogs'