import flask

from flask import url_for, Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')             # With this single entry, you can comment out the rest of the lines
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:                                  # Create a function to store the data rxed in forms in database.txt
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file=database.write(f'\n {email}, {subject}, {message}')


@app.route('/submit_form', methods=['POST', 'GET']) # For this to work, make some changes to the contact.html under <send> tab# See changes in line 75 and 62
#def submit_form():
#    return 'Form Submitted! Thank you!'
def get_data():                                  # Use this function to get the contact data posted by the e-mail client
    if request.method == 'POST':
        data=request.form.to_dict()
        write_to_file(data)                     # Call this function to store the data in database.txt
        print(data)
        return redirect('/thankyou.html')       # import redirect method for this 
    else:
        return 'something went wrong'


#@app.route('/works.html')
#def works():
#    return render_template('works.html')

#@app.route('/work.html')
#def work():
#    return render_template('work.html')

#@app.route('/about.html')
#def about_us():
#    return render_template('about.html')

#@app.route('/contact.html')
#def contact():
#    return render_template('contact.html')

#@app.route('/components.html')
#def component():
#    return render_template('components.html')