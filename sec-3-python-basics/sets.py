# set - unordered collection of unique objects 
# NO DUPLICATES in a set 

my_set = {30, 60, 90,  120, 150, 150}

your_set = {120, 150, 180, 210}

print(my_set)

# O/P: {150, 120, 90, 60, 30} - See here; No Duplicates!!!!! 

my_set.add(180)
print(my_set)

# O/P: {180, 150, 120, 90, 60, 30}

# QUESTION: How to convert a list into a set? 

test_list = [3, 6, 9, 12, 15, 15]

print(set(test_list))

# O/P: {3, 6, 9, 12, 15} - Removes the duplicate !!

# How to access an entry/value in set? 

#print(my_set[0])

# O/P: Traceback (most recent call last):
#  File "sets.py", line 25, in <module>
#    print(my_set[0])
# TypeError: 'set' object is not subscriptable

print(30 in my_set )

# O/P: True

new_set = my_set.copy()
print(new_set)

# O/P: {180, 150, 120, 90, 60, 30}

# Sets Methods 

print(my_set.difference(your_set)) # NOTE: Does NOT modify the set itself!! 
# O/P: {90, 60, 30}

print(my_set)

# O/P: {180, 150, 120, 90, 60, 30}

# To discard a set entry use my_set.discard(<value>)

print(my_set.difference_update(your_set))
# O/P: None 

print(my_set)
# O/P: {90, 60, 30}

# Other methods in a set:

#my_set.intersection()
#my_set.union()  # Removes duplicates 
#my_set.issubset(your_set)
#my_set.issuperset(your_set)




