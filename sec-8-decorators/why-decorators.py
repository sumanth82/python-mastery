# @performance decorator to see how long my testing runs, how many ms it takes to complete

from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()       # To store the time of the beginning of the function
        result = func(*args, **kwargs)
        t2 = time()       # To store the time of the end of the function
        print(f'It took {t2-t1} ms long to run')
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000000):
        i*5


long_time()

# O/P: It took -0.4681270122528076 ms long to run
