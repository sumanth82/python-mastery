# A basic decorator MUST and SHOULD follow this syntax to be called-or-used as a decorator;


# This is the SYNTAX THAT MUST BE FOLLOWED to create a decorator


def my_decorator(func):
    def wrap_func():
        print('*****')
        func()
        print('*****')
    return wrap_func


# Essentially it's like calling a decorator function and adding it to the hello() function
@my_decorator
def hello():
    print('hello')


hello()

# O/P: *****
# hello
# *****


def my_decorator2(func2):
    def wrap_func2(*args, **kwargs):
        print('##########')
        func2(*args, **kwargs)
        print('##########')
    return wrap_func2


# When you call the decorator, you pass the succeeding function to the decorator i.e func2 gets hello2() as argument

@my_decorator2
def hello2(greeting, emoji=';-)'):
    print(greeting, emoji)


hello2('Greetings from NC')


# O/P: ##########
# Greetings from NC; -)
##########
