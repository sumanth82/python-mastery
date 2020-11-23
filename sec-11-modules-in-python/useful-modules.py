# Useful built-in and custom modules

from collections import Counter, defaultdict, OrderedDict

import datetime

from time import time

li = [1, 2, 3, 4, 5, 6, 7, 7]

print(Counter(li))

# O/P: Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
# Counter creates a Dict that keeps track of how many times a key showed up in an iterable
# Useful for duplicate e-mails etc..
# Useful for converting list to a dict


# defaultdict - Used to assign a value to a dict key if none exists


test_dict = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(test_dict['c'])

# O/P: 5
print(test_dict)

# O/P: defaultdict(<function <lambda> at 0x10e12b7a0>, {'a': 1, 'b': 2, 'c': 5})

# OrderedDict maintains the order of the dict unlike the default dict data type

d = {}
d['a'] = 1
d['b'] = 2

d1 = OrderedDict()

d1['a'] = 1
d1['b'] = 2

print(d1 == d)

# O/P: True


# P.S: dict is unordered sets

print(datetime.time(5, 45, 00))

# O/P: 05:45:00
# Helps to print a custom date

print(datetime.date.today())

# O/P: 2020-11-23
