# utility is a module
import utility

# shopping_cart is a module as it's within a folder - shopping
# import shopping_cart            # This will throw the error below

# O/P: Traceback (most recent call last):
# File "main.py", line 5, in <module >
# ModuleNotFoundError: No module named 'shopping_cart'

# Instead the right thing to do is:

# import < package_name >.< module_name >

import shopping.shopping_cart

print(shopping.shopping_cart)

# O/P: <module 'shopping.shopping_cart' from '/Users/sumantrenukarya/SUMANT/TECH/Python-Projects/python-mastery/sec-11-modules-in-python/module-sample/shopping/shopping_cart.py'

print(shopping.shopping_cart.buy('apple'))

# O/P: ['apple']

print(utility)
print(utility.multiply(2, 3))

# O/P: <module 'utility' from '/Users/sumantrenukarya/SUMANT/TECH/Python-Projects/python-mastery/sec-11-modules-in-python/module-sample/utility.py'>
# 6
