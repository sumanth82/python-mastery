# reduce(<function>, <sequence_or_data>)
from functools import reduce

my_list = [1, 2, 3]


def multiple_by2(item):
    return item*2


def check_odd(item):
    return item % 2 != 0


def accumulator():
