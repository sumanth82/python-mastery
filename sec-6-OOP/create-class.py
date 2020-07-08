# Define a class - PlayerCharacter

class PlayerCharacter:
    def __init__(self, name):           # This is a init method; Defines the char name; __init__ is a special method (dunder method or a magic method) This is often called a init method or a constructor method
                                        # This is automatically called, everytime we instantiate a class/this class. 
        self.name = name                # self is the way for us to define self i.e name of the class = PlayerCharacter; 
                                        # Here, name = attributes or the properties the objects have and you can access them by doing the .<attribute_name>. Ex: player1.name

    
    def run(self):                      # New 'run' method; that each player can run ==> To access a method you use, .run()
        print('run')

# Instantiate the class through an object/instance player1

player1 = PlayerCharacter('Cindy')
print(player1)

print(player1.name)

# O/P:

#<__main__.PlayerCharacter object at 0x106560350>
#name

# O/P if you don't pass 'Cindy' to the PlayerCharacter: 

#Traceback (most recent call last):
#  File "create-class.py", line 12, in <module>
#    player1 = PlayerCharacter()
#TypeError: __init__() missing 1 required positional argument: 'name'


# The reason for the above error with the init method is you haven't passed a parameter when instance player1 is created


