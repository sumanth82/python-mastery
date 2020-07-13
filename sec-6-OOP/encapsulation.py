# Encapsulation - Binding of data and functions that manipulate this data; This data and functions in a class is called attribtes and methods
# You essentially encapsulate the functionality 

# Abstraction: Hiding of info or abstracting away the info and give only what's useful 

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def speak(self):
        return (self.name)

player1 = PlayerCharacter('Andrei', '100')
print(player1.age)  # O/P: 100

print(player1.speak)    # O/P: <bound method PlayerCharacter.speak of <__main__.PlayerCharacter object at 0x10be83390>>
print(player1.speak())  # O/P: Andrei 

player1.speak = 'BOOO'
print(player1.speak)    # O/P: BOOO ; This is BAD; It Negates the class and the method/function defined in the class. 


# Public and Private Variables:
# There is no concept of private or public variables in Python and hence line 21 andd 22 works just fine negating the method defined within the class. 

# How to overcome? 

# _name, _age is the naming convention within the class to say this is a private variables; However this NOT guaranteed to be overwritten ;
# E.g:

class PlayerCharacter2:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return print(f'My name is {self._name}'


player2=PlayerCharacter2('Andrei', '100')
print(player2.name)

print(player2.speak())











