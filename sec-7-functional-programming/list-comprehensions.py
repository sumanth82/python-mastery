# list, set or dictionary comprehensions

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# O/P: ['h', 'e', 'l', 'l', 'o']

# Instead of the above format, use list-comprehensions as below:

my_list1 = [char for char in 'hello']
print(my_list1)

# O/P: ['h', 'e', 'l', 'l', 'o']
