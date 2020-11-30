import re

string = 'search inside of this text please'
print('search' in string)

# O/P: True
print(re.search('this', string))

# O/P: <re.Match object; span=(17, 21), match='this'>
# Gives the index of occurrence of the specific string

a = re.search('this', string)
print(a.span())

print(a.start())

print(a.end())

print(a.group())

# O/P: (17, 21)
# 17
# 21
# this

string1 = 'search this inside of this text please'

pattern = re.compile('search this')

a = pattern.search(string1)
b = pattern.findall(string1)
c = pattern.fullmatch(string1)  # To search the exact string entry
d = pattern.match(string1)  # To search a portion of the string entry

print(a)
print(b)
print(c)
print(d)
# <re.Match object; span=(7, 11), match='this'>
#['this', 'this']
# None
