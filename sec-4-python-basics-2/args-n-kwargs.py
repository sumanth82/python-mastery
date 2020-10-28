# use *args to pass any number of arguments to a function 
# use **kwargs to pass any number of key-value pairs as arguments to a function 

def super_func(*args):
    print(args)
    # (1, 2, 3, 4, 5)
    return sum(args)

print(super_func(1,2,3,4,5))
# O/P: 15

def super_func2(*args, **kwargs):
    print(kwargs)
    # O/P: {'age1': 15, 'age2': 30}
    total = 0
    for i in kwargs.values():
        total += i
    return sum(args) + total

print(super_func2(1,2,3,4,5, age1=15, age2=30))

# O/P: 60