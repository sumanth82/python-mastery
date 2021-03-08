# Let's remove the stories with less than 100 points in the below website:
# https://news.ycombinator.com/

# You use Beautiful Soup - Allows us to use html and grab the data from it
# https://www.crummy.com/software/BeautifulSoup/bs3/download/2.x/documentation.html


# Install beautifulsoup4 and requests

# pip3 install beautifulsoup4
# pip3 install requests

import requests
import pprint

from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
print(res)
print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
print(type(soup))
# O/P: <class 'bs4.BeautifulSoup'>
# print(soup)

links = soup.select('.storylink')
subtext = soup.select('.subtext')

# print(links)
print(type(links))
# O/P: <class 'bs4.element.ResultSet'>

votes = soup.select('.score')


def create_custom_hn(links, subtext):
    hn = []                                 # hn = hackernews
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            print(points)
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

        # O/P:  125
        #        387
        #        56
        #        45
        #        31

            # hn.append(href)  # This prints the web URL's
            # hn.append(title)    # This prints the titles

    return hn


pprint.pprint(create_custom_hn(links, subtext))

# O/P: {'link': 'https://twitter.com/wongmjane/status/1335198021131194370',
#  'title': 'Cloudflare working on Cloudflare Pages, for deploying and hosting '
#           'JAMstack',
#  'votes': 94},
# {'link': 'https://github.com/Piraxus/Skybolt',
#  'title': 'Skybolt: A C++ planetary environment rendering engine with Python '
#           'bindings',
#  'votes': 130}]
