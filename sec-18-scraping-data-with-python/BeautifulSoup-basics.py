# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# CSS Selectors

# https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors


import requests

from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
print(res)

print(res.text)

print(type(res.text))

# O/P: <class 'str'>
# O/P: is a string object

# Convert the string object to a html format using BeautifulSoup

soup = BeautifulSoup(res.text, 'html.parser')

print(soup)

print(type(soup))

# O/P: <class 'bs4.BeautifulSoup'>

# Now, in the html output format you can just list the contents or the body or the title

print(soup.body)

print(soup.body.contents)

print(soup.find_all('a'))

# O/P: [ <a href="security.html">Security</a>, <a href="http://www.ycombinator.com/legal/">Legal</a>, <a href="http://www.ycombinator.com/apply/">Apply to YC</a>, <a href="mailto:hn@ycombinator.com">Contact</a>]

# Lists all the links on the page as a list

print(soup.find('a'))


# O/P: Prints out the first link
# O/P: <a href="https://news.ycombinator.com"><img height="18" src="y18.gif" style="border:1px white solid;" width="18"/></a>

print(soup.find(id='score_25283971'))

# O/P: <span class="score" id="score_25283971">267 points</span>


# You can use css selectors to grab a list of objects in html
print(soup.select('a'))

print(soup.select('.score'))

# O/P: [ <span class="score" id="score_25283848">63 points</span>, <span class="score" id="score_25285117">30 points</span>, <span class="score" id="score_25285333">124 points</span>]

links = print(soup.select('.storylink'))

# O/P: [class="storylink" href="https://www.bbc.com/news/world-us-canada-55164607">Baby girl born from record-setting 27-year-old embryo</a>, <a class="storylink" href="https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md">Kubernetes is deprecating Docker runtime support</a>]

print(soup.select('.storylink')[0])

# O/P: <a class="storylink" href="https://returntonow.net/2018/01/11/7-ways-mushrooms-can-save-world/">Mushrooms Can Eat Plastic, Petroleum and CO2 (2018)</a>

links = (soup.select('.storylink'))
votes = soup.select('.score')

print(votes[0])

# O/P: <span class="score" id="score_25286678">151 points</span>

print(votes[0].get('id'))

# O/P: score_25286678
