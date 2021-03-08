# LET's SORT the data now

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

soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

votes = soup.select('.score')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


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

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))

# [{'link': 'https://www.spectator.co.uk/article/the-grenfell-tower-inquiry-is-uncovering-a-major-corporate-scandal/',
# 'title': 'The Grenfell Tower inquiry is uncovering a major corporate scandal',
#  'votes': 397},
# {'link': 'https://arxiv.org/abs/2012.00152',
#  'title': 'Every Model Learned by Gradient Descent Is Approximately a Kernel '
#           'Machine',
#  'votes': 311},
# {'link': 'https://emacsconf.org/2020/talks/',
#  'title': 'EmacsConf 2020 Talks',
#  'votes': 270},
