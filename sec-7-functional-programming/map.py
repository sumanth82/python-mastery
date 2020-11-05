# map - map(<function_name>, <iterables to pass to the the function>)
# map() - Allows to create a new list as an argument instead of defining an argument

def multiple_by2(item):
    return item*2


print(list(map(multiple_by2, [1, 2, 3])))
# O/P: [2, 4, 6]
