# reduce(<function>, <sequence_or_data>, <initial_data>)
# reduce allows us to reduce something, some value from the iterable that we're giving
# USE CASE: Reduce a list to a single data - like in the example below, returns the sum of the my_list

from functools import reduce

my_list = [1, 2, 3]


def multiple_by2(item):
    return item*2


def check_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print((reduce(accumulator, my_list, 0)))

print(my_list)


# O/P: 0 1
# 1 2
# 3 3
# 6
#[1, 2, 3]
