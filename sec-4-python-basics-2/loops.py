for item in ['a', 'b', 'c']:
    print(item)

print(item)

# O/P: a
#b
#c
#c

# ITERABLES:

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for key, value in user.items():
    print(key, value)


# O/P: name Golem
#age 5006
#can_swim False

for i in user.keys():
    print(i)

# O/P: name
#age
#can_swim

for i in user.values():
    print(i)

# O/P: Golem
#5006
#False