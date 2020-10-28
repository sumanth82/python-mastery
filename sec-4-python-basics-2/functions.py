# parameters

def say_hello(name, emoji):
    print(f'Hellooo {name} {emoji}')

#arguments or # positional arguments
say_hello('Timon', ';-)')

# O/P: Hellooo Timon ;-)

# keyword arguments (pass the parameters and the arguments in the function call)

say_hello(name='Bibi', emoji=':-)')

##### return in functions #####

def sum(num1, num2):
    num1 + num2

sum(4, 5)
print(sum(4,5))
# O/P: None

def sum1(num1, num2):
    return num1 + num2

print(sum1(5, 5))
# O/P: 10

total = sum1(30, 30)
print(total)
# O/P: 60

print(sum1(100, total))
# O/P: 160

# If a function returns a value, you can assign that to a variable outside the function.


# Defining a function within a function and the return statements:

def sum2(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

total2 = sum2(10, 20)
print(total2)   # O/P: 30
