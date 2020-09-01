# http://www.mashup-template.com/templates.html

# Pick a sample free, ready html template to build your website 

# I will create the portfolio project in /portfolio-project folder
# unzip a univers-html.zip file 

# Step-1 : setup a flask env:

# cd to root-level - (i.e sec19-web-development)
# python3 -m venv portfolio-project/ (web-server folders acts a venv, installs bin, lib and include folders)
# cd portfolio-project/bin
# ./activate

# Step - 2: move all css, js and assets folder to static, index.thml to templates

# Step -3 : create the routes in the portfolio.py file

# Step-4:

# export FLASK_ENV=development
# export FLASK_APP=portfolio.py
# flask run

# Free templates websites:
# https://www.creative-tim.com/bootstrap-themes/ui-kit?direction=asc&sort=price
# https://html5up.net/

# HOW to GENERATE THE ROUTES dynamically instead of to specifying for each end-point?

# Answer : See below

#Ex:

#@app.route('/string:page_name)')

#def html_page(page_name):
#    return render_template(page_name)

#####

## How to SUBMIT a FORM! 

# You use the request object in flask

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data


#### Once you submit the contact us info or something, how to store that on the server?

## Once you submit the data, to capture on the server the form, needs to have name entry. 

# Mainly line 67-70

'''

 <input type="email" class="form-control" id="email" placeholder="Email">
                      </div>
                      <div class="form-group">
                        <input type="text" class="form-control" id="subject" placeholder="Subject">

'''

## After the data is submitted by user, rxed by the server, send a response/acknowledgement to thank you

#This is done using the redirect() module


'''

@app.route('/submit_form', methods=['POST', 'GET']) # For this to work, make some changes to the contact.html under <send> tab# See changes in line 75 and 62
#def submit_form():
#    return 'Form Submitted! Thank you!'
def get_data():                                  # Use this function to get the contact data posted by the e-mail client
    if request.method == 'POST':
        data=request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')

'''

## Storing the received data in persistent data store 

### TO grab and store the data in the backend, in the html file, you need to add name= parameter for the submit form fields
# 
#  Like below:

'''

<div class="form-group">
                        <input name="email" type="email" class="form-control" id="email" placeholder="Email">
                      </div>
                      <div class="form-group">
                        <input name="subject" type="text" class="form-control" id="subject" placeholder="Subject">
                      </div>
                      <div class="form-group">
                        <textarea name="message" class="form-control" rows="5" placeholder="Enter your message"></textarea>
                      </div>
                      <button type="submit" class="btn btn-default btn-lg">Send</button>

'''

# After this, you will have a Form Data Field in the developer's tools '

'''

email: sumanth82@gmail.com
subject: sdfds
message: sdfds

'''

## To access this data you can use the request.forms in flask

# building-a-portfolio-6

# To store the data, create a file called - database.txt

# building-a-portfolio-7 ; Instead of writing the file to txt. write it to csv



