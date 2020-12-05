# Let's remove the stories with less than 100 points in the below website:
# https://news.ycombinator.com/

# You use Beautiful Soup - Allows us to use html and grab the data from it
# https://www.crummy.com/software/BeautifulSoup/bs3/download/2.x/documentation.html


# Install beautifulsoup4 and requests

# pip3 install beautifulsoup4
# pip3 install requests

import requests

from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
print(res)

print(res.text)


# O/P: <Response [200]>
# <html lang="en" op="news"><head><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" type="text/css" href="news.css?jQhI4QM59GzYU3FIHxj3">
# <link rel="shortcut icon" href="favicon.ico">
