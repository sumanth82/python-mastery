# NOTE: List re-assignment is very important; Both the lists take the same value based on the data in the memory

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']

print(amazon_cart[0:2])     
# O/P: ['notebooks', 'sunglasses']

print(amazon_cart[0:3:2])
# O/P: ['notebooks', 'toys']

new_cart = amazon_cart
# With this you just assing the value of new_cart to be the value of amazon_cart in MEMORY !!

print(new_cart)
# ['notebooks', 'sunglasses', 'toys', 'grapes']

print(amazon_cart)
# ['notebooks', 'sunglasses', 'toys', 'grapes']

new_cart[0]='pencils'

print(new_cart)
# O/P: ['pencils', 'sunglasses', 'toys', 'grapes']

print(amazon_cart)
# O/P: ['pencils', 'sunglasses', 'toys', 'grapes']

'''IMPORTANT  - If you want to retain your original list and just copy the contents of the original list to the new list, use below'''

new_list = amazon_cart[:]     ## COPY the contents of the original list - amazon_cart[] to new_list[] but do NOT change this original amazon_cart[]

print(new_list)


new_list[0] = 'ink'
print(new_list)
# ['ink', 'sunglasses', 'toys', 'grapes']

print(amazon_cart)
# ['pencils', 'sunglasses', 'toys', 'grapes']

# List slicing creates a new list.

print(amazon_cart[::-1])

# O/P: ['grapes', 'toys', 'sunglasses', 'pencils']

print(amazon_cart) # NOTE: This is extremely important

# O/P: ['pencils', 'sunglasses', 'toys', 'grapes']


# RANGE!!!!!!!  format - (start, stop-1)
# Default if you don't specify start is 0

print(list(range(1, 10)))
# O/P: [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(10)))

# O/P: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# .join() method - acts on strings and needs to be 

# LIST to STRING!!!!! 
name = ''

print(name.join(['Hello', 'Sumant']))

# O/P: HelloSumant








