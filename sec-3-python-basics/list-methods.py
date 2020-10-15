# List does an IN-PLACE assignment ONLY;

basket = [1,2,3,4,5]

# append
new_list = basket.append(100)

print(new_list)
# O/P: None

print(basket)
# O/P: [1, 2, 3, 4, 5, 100]

#insert at a specific index - DOES NOT REPLACE THE VALUE IN CURRENT INDEX; 

basket.insert(0, 500)
print(basket)

# O/P: [500, 1, 2, 3, 4, 5, 100]

# extend - similar to append, can append multiple list values 

basket.extend([200, 300])

print(basket)

# [500, 1, 2, 3, 4, 5, 100, 200, 300]

# pop - Pops off what's at the end of the list

print(basket.pop()) # O/P: 300

print(basket)
# O/P: [500, 1, 2, 3, 4, 5, 100, 200]

print(basket.pop(0))    # pop off or remove the value at index 0 
# O/P: 500

print(basket)
# O/P: [1, 2, 3, 4, 5, 100, 200]

# remove - remove a specific value from the list 

basket.remove(200)

print(basket)
# O/P: [1, 2, 3, 4, 5, 100]

# clear - removes all the entries in a list

basket.clear()

print(basket)
# O/P: []

# index - gives the index value 
# .index(<object_name>, <index_start_point>, <index_end_point>)

test_basket = ['a','b','c','d','e']

print(test_basket.index('d'))       
# O/P: 3

print(test_basket.index('d', 0))

# O/P Traceback (most recent call last):
#  File "list-methods.py", line 64, in <module>
#    print(test_basket.index('d', 0, 2))
#ValueError: 'd' is not in list


# count() - How many times a char/value occurs; 
print(test_basket.count('e'))

# O/P: 1

new_basket = ['p', 'a', 'q', 'e', 'c']

print(sorted(new_basket))           # IN-PLACE SORTED() function ONLY; Does not Update the List 
# O/P: ['a', 'c', 'e', 'p', 'q']

print(new_basket)
# O/P: ['p', 'a', 'q', 'e', 'c']

new_basket.sort()
print(new_basket)

# O/P: ['a', 'c', 'e', 'p', 'q']

# reverse() method - Just reverses

new_basket.reverse()
print(new_basket)

# O/P: ['q', 'p', 'e', 'c', 'a']





