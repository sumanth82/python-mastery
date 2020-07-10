#declarator for the method in a class using -  @classmethod
# similar to adding attributes to the class, this is for methods
# 

class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def shout(self):
        print(f'My name is {self.name}')
    
    @classmethod                            # You define a class method using - @classmethod
    def adding_things(cls, num1, num2):     # By default, the first argument is a cls - stands for a class. 
        return num1 + num2
    
    @staticmethod                           # No access to the class or the class object
    def adding_things2(num1, num2):         # stand-alone method
        return num1 + num2 
    
    
player1=PlayerCharacter('Tom', 20)
print(player1.adding_things(2, 3))      # O/P: 5 

print(player1.adding_things2(6, 6))     # O/P: 12





