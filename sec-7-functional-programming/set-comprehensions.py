# set and dict comprehensions

# set comprehensions example:

my_list = {char for char in 'hello'}

print(my_list)

# O/P: {'o', 'h', 'e', 'l'}

# dict comprehensions

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)

# O/P: {'a': 1, 'b': 4}

my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)

# O/P: {1: 2, 2: 4, 3: 6}
