print(type(''))

# O/P: <class 'str'>;
# Every Object is denoted as a class in Python 

print(type('hi'.lower()))

# Objects have different methods to perform some actions on them - like lower() etc.. AND attributes that you can access with . method
# 
#  

# class is a blueprint 
# object is defined based off class 

class BigObject:                             # camel-case - Every word begins with a UpperCase for a class name
    pass
print(type(BigObject))

# O/P: <class 'type'>

# Instantiate the class created above

obj1 = BigObject()          # () - denotes a class; This is creating a new instance/new object of the class BigObject()
print(type(obj1))

obj2 = BigObject()
obj3 = BigObject()


# O/P: <class '__main__.BigObject'>








