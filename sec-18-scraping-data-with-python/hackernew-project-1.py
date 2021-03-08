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

soup = BeautifulSoup(res.text, 'html.parser')
print(type(soup))
# O/P: <class 'bs4.BeautifulSoup'>
# print(soup)

links = soup.select('.storylink')

# print(links)
print(type(links))
# O/P: <class 'bs4.element.ResultSet'>

votes = soup.select('.score')


def create_custom_hn(links, votes):
    hn = []                                 # hn = hackernews
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        points = int(votes[idx].getText().replace(' points', ''))
        print(points)

        # O/P:  125
        #        387
        #        56
        #        45
        #        31
        #    Traceback(most recent call last):
        #        File "hackernew-project-1.py", line 48, in <module >
        #        create_custom_hn(links, votes)
        #    File "hackernew-project-1.py", line 40, in create_custom_hn
        #    points = int(votes[idx].getText().replace(' points', ''))
        #    IndexError: list index out of range

        # NOTE: In-order to fix the above, look into hackernew-project-2.py

        # hn.append(href)  # This prints the web URL's
        # hn.append(title)    # This prints the titles
        hn.append({'title': title, 'link': href})
    return hn


create_custom_hn(links, votes)

# O/P: {'title': 'Vanishing zeroes for geometric algebra in Rust', 'link': 'https://fanf.dreamwidth.org/134024.html'}, {'title': 'Skybolt: A C++ planetary environment rendering engine with Python bindings', 'link': 'https://github.com/Piraxus/Skybolt'}]
