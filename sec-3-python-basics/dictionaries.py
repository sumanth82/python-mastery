# Hash Table
# Map
# Objects 
# un-ordered key value pair
# written/scattered in different places in memory unlike a list 

# dict keys need to be immutable; You CANNOT have list as a key
dictionary = {
    'a': 1,
    'b': [10, 20, 30]
}

print(dictionary['b'][1])

# O/P: 20

test_list = [{'a': 12, 'b': 13}, {'a': 22, 'b': 23}]

print(test_list[1]['a'])
# O/P: 22

################### IMP!!! using the dict.get() method for dict keys #########

#print(dictionary['age'])

# O/P: Traceback (most recent call last):
#  File "dictionaries.py", line 24, in <module>
#    print(dictionary['age'])
#KeyError: 'age'

#The above prints out an error with no KeyError ; 

# Instead to find if a key exists or not, use this - dict.get() method

print(dictionary.get('age'))

# O/P: None 

# If you want to assign a default value to a key AND if the key doesn't exist in a dict, use the below:

print(dictionary.get('age', 55))

# O/P: 55

print(dictionary)

# O/P: {'a': 1, 'b': [10, 20, 30]}

# Another format to create a dictionary

user2=dict(name='Tesla', age = 5)
print(user2)

# O/P: {'name': 'Tesla'}

## How to find if a key exists in a dict? 

print('basket' in dictionary)

# O/P: False

############## USING DICT METHODS to play with keys and values !!!!!!!!!!! ####

print('age' in user2.keys())
# O/P: True

print(5 in user2.values())

# O/P: True 

# To get all the items: 

print(user2.items())

# O/P: dict_items([('name', 'Tesla'), ('age', 5)])

# To delete or clear an existing dictionary: 

#print(user2.clear())

# O/P: None

#print(user2)

# O/P: {}

### COPY() method

user3 = user2.copy()

print(user3)
# O/P: {'name': 'Tesla', 'age': 5}

# To remove a specific key, value in a dict - use dict.pop(<key>)

print(user3.pop('age'))

# O/P : 5

print(user3)

# O/P: {'name': 'Tesla'}

# To update a dict entry or add a new k, v pair - use - dict.update()

user2.update({'age': 8})
print(user2)

# O/P: {'name': 'Tesla', 'age': 8}

user2.update({'Made in': 'California'})

print(user2)

# O/P: {'name': 'Tesla', 'age': 8, 'Made in': 'California'}