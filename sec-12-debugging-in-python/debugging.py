# Linting - Helps to detect discrepancy in code before running it
# pdb - Python Debugger - Interactive Python Debugger to test your code during the runtime
# Use breakpoint()

import pdb


def test_func(num1, num2):
    # pdb.test_trace()
    breakpoint()
    return num1 + num2


test_func(4, 'sdfkghsdkfjs')


# O/P: -> return num1 + num2 - Gives an interactive display of the values/arguments for each parameter passed to the func.
# (Pdb) num1
# 4
# (Pdb) num2
# 'sdfkghsdkfjs'
# (Pdb) help - Displays help

# (Pdb) step --> GOES TO THE NEXT LINE after breakpoint()

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# > / Users/sumantrenukarya/SUMANT/TECH/Python-Projects/python-mastery/sec-12-debugging-in-python/debugging.py(11)test_func()
# -> return num1 + num2


# (Pdb) a  --> LISTS all the arguments
# num1 = 4
# num2 = 'sdfkghsdkfjs'


# (Pdb) w   --> Shows WHERE WE ARE WITH THE CONTEXT
# /Users/sumantrenukarya/SUMANT/TECH/Python-Projects/python-mastery/sec-12-debugging-in-python/debugging.py(14) < module > ()
# -> test_func(4, 'sdfkghsdkfjs')
# > / Users/sumantrenukarya/SUMANT/TECH/Python-Projects/python-mastery/sec-12-debugging-in-python/debugging.py(11)test_func()
# -> return num1 + num2

# (Pdb) next   --> Goes to the NEXT CONTEXT
# --Return--
# > / Users/sumantrenukarya/SUMANT/TECH/Python-Projects/python-mastery/sec-12-debugging-in-python/debugging.py(11)test_func() -> None
# -> return num1 + num2
