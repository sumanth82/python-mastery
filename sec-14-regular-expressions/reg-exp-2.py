import re

string1 = 'search this inside of this text please'

pattern = re.compile(r"([a-zA-Z]).([a])")

a = pattern.search(string1)
b = pattern.findall(string1)
c = pattern.fullmatch(string1)  # To search the exact string entry
d = pattern.match(string1)  # To search a portion of the string entry

print(a)
print(b)
print(c)
print(d)


print(a.group())
print(a.group(1))
print(a.group(2))


# O/P:
# <re.Match object
# span = (0, 3), match = 'sea' >
#[('s', 'a'), ('l', 'a')]
# None
# <re.Match object
# span = (0, 3), match = 'sea' >
# sea
# s
# a
