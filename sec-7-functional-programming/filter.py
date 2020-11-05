# filter() - Receives a True or False value;
# If True or False will keep it in the list

my_list = [1, 2, 3]


def check_odd(item):
    return item % 2 != 0


print(list(filter(check_odd, my_list)))

# O/P: [1, 3] - Returns ONLY odd values from the function

print(my_list)

# O/P: [1, 2, 3]
