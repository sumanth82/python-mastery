# Flask has this other rule called Variable Rules

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules

# Let's say you want the website to list the blogs of individual users:

# www.testblog.com/sandeep
# www.testblog.com/Timon 

# The username endpoint should be dynamic 

# How to do this in index.hmtl? - Using <variable> syntax - see index.html 

# You can also pass integers 

# Ex: 

#@app.route('/<username>/<int:post_id>')           # You pass the <username> var value fetched from the website user to the function which calls index.hmtl

#def index(username=None, post_id=None):
#    return render_template('index.html', name=username, post_id=post_id)

# www.testblog.com/Timon/23 
# http://127.0.0.1:5000/Sumant/2
