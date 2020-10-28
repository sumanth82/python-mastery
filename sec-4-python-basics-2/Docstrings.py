# Using Docstrings within a function (''' ''') allows the function defn to be displayed when calling the function 

def test(a):
    '''
    Info: tests and prints param a
    '''
    print(a)

test('!!!!!')

# O/P: !!!!!

#test()

#help(test)  # USE THIS to get help on a function!! 

# O/p: Help on function test in module __main__:

#test(a)
#    Info: tests and prints param a

# Use: 
# 
# Or 

print(test.__doc__)

# O/P: Info: tests and prints param a