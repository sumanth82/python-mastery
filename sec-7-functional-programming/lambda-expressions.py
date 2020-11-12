# One time anonymous, nameless functions that you don't need more than once;
# lambda expressions
# Format:

# lambda param: func/action(param)

def identity(x):
    return x*10


print(identity(10))

# O/P: 100

t1 = (lambda x: x*2)

print(t1(4))

# O/P: 8
