# An error that crashes a program highlighting the errors is an exception.

# Python built-in exceptions : https://docs.python.org/3/library/exceptions.html

# Error handling allows the script to continue with the exec even if there is an error and NOT crash the program.

#age = int(input('Enter your age: '))
# print(age)

# Enter your age: kfkf
# Traceback(most recent call last):
#    File "error-handling.py", line 7, in <module >
#    age = int(input('Enter your age: '))
# ValueError: invalid literal for int() with base 10: 'kfkf'

# How to handle the above error?


try:
    age = int(input('Enter your age: '))
    print(age)
except ValueError:
    print('Please enter your age in digits and NOT any other alphanumeric char')
except ZeroDivisionError:
    print('please enter age above 0')


# O/P: Enter your name: sdfsdkdksd
# Please enter your age in digits and NOT any other alphanumeric char
def sum(num1, num2):
    try:
        return num1 + num2
    # err - a variable that store the exception and can be used to print meaningful messages
    except (TypeError, ZeroDivisionError) as err:
        print(f'Please enter only numbers {err}')
    finally:
        print('okay, you are all done!')


print(sum(1, '2'))

# O/P: Please enter only numbers unsupported operand type(s) for +: 'int' and 'str'
# okay, you are all done!


# To raise your own exception or error, use raise as below:


try:
    return num1 + num2
    raise Exception('Hey cut it out')
    # err - a variable that store the exception and can be used to print meaningful messages
    except (ZeroDivisionError) as err:
        print(f'Please enter only numbers {err}')
