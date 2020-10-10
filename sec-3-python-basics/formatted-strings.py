name = 'Johnny'
age = '20'

print('Hi I am ' + name + ' I am ' + age + ' years old')

# O/P: Hi I am Johnny I am 20 years old

## ALTERNATIVE for the above is a formatted string

print(f'Hi I am {name} and I am {age} years old')

# O/P: Hi I am Johnny and I am 20 years old

## Older .format() method; This worked in Python2

print('Hi I am {} and I am {} years old'.format(name, age))

# Hi I am Johnny and I am 20 years old

print('Hi I am {new_name} and I am {age}'.format(new_name='Sally', age='100'))

# Hi I am Sally and I am 100


