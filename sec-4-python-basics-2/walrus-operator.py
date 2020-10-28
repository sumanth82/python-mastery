# walrus (:=)
# assign value to a variable after evaluating an expression
# Valid only in Python 3.8 
a = 'helloooooooooo'

if ((n := len(a)) > 10):
    print(f'Too long {n} elements')

