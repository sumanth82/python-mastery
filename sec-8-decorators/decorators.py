# Anything following an @ symbol is a decorator
# Ex: @staticmethod
# @classmethod

# They essentially use functions under the hood;
# Decorators super charge our functions; Provides extra features to our functions

# Higher Order Function (HOC) - Accepts another function within that function;
# It either accepts another function as an argument or returns another function

def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func
