# Tuples are Immutable lists - CANNOT be changed once created 
# Use case - When you don't want developers to change the entries in a given variables
# Tuples are faster than list as you can't operate on tuples (like reverse, sort) unlike lists 

my_tuple = (1, 5, 10, 15, 20)
print(my_tuple[2])

# O/P: 10

# Tuple slicing: 

new_tuple = my_tuple[1:2]

print(new_tuple)

# O/P: (5,)

new_tuple2 = my_tuple[2:]

print(new_tuple2)

# O/P: (10, 15, 20)

# How to assign key, values to a tuple

x , y, z, *others = (100, 200, 300, 400, 500, 600)

print(x)

# O/P: 100

print(others)

# O/P: [400, 500, 600]

# Methods in a tuple - .index() and .count()

print(my_tuple.count(5))

# O/P: 1

print(my_tuple.index(5))

# O/P: 1

