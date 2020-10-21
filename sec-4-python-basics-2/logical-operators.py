# and 
# or 
# >
# <
# == 

print(4<5)

# O/P: True 

print(not(True))
# False 

is_magician = False
is_expert = True

# check if magician AND expert; If so print 'You are a master'
# check if magician but NOT expert; If so, print 'atleast you're getting there!!'
# 'if you're not a magician'; print 'You need magic powers'


#char1 = ('You are a master') if is_magician and is_expert
#print(char1)

if is_expert and is_magician:
    print('You are a master')
elif is_magician and not is_expert:
    print('atleast you\'re getting there!!')
elif not is_magician:
    print('You need magic powers')

# O/P: You need magic powers


print(True == 1)
print('' == 1)
print([] == 1 )
print(10 == 10.0)
print([] == [])

# O/P: True
#False
#False
#True
#True

name = ['Harry']
surname = ['Harry']

print(name is surname)

# O/P: False
#### IMP: Everytime a new list is created, it takes a different memory space than the other list and lists can NEVER be true for the above

print(name == surname)
# O/P: True 