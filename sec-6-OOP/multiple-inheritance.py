class User():
    
    def sign_in(self):
        print('logged in')

class Wizard(User):         # class Wizard inherits class User and all the methods of User class are available here in Wizard class
    def __init__(self, name, power):
        self.name=name
        self.power=power
    
    def attack(self):
        print(f'attacking with power of {self.attack}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name=name
        self.arrows=arrows
    
    def check_arrows(self):
        print(f'{self.arrows} remaining')
    
    def run(self):
        print(f'ran really fast')

#class HybridBorg(Wizard, Archer):    # This class inherits multiple classes and the methods in them
#    pass

#hb1 = HybridBorg('Borgie', 50, 100)
#print(hb1.run())

# O/P: ran really fast
# None

# If you try to run a method from class Acher now, it wont work. 

#print(hb1.check_arrows())

# O/P: AttributeError: 'HybridBorg' object has no attribute 'arrows' - When - HybridBorg('Borgie', 50)
# O/P: TypeError: __init__() takes 3 positional arguments but 4 were given - When - HybridBorg('Borgie', 50, 100)

# To solve this, you define a __init__ method in the new class HybridBorg


class HybridBorg(Wizard, Archer):    # This class inherits multiple classes and the methods in them
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg('borgie', 50, 100)
print(hb1.check_arrows())

# O/P: 100 remaining

print(hb1.attack())








