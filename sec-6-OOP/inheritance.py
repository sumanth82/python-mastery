# Child classes are also called sub classes or derived classes:

class User():
    
    def sign_in(self):              # NOTE: No __init__ method defined at the beginning of the class coz no identifiers or the variables to define and pass to the class.
        print('Logged in as user')

class Wizard(User):                     # How to ensure these 2 classes has the users initially signed in without explicitly defining? ANS: Inherit the class - User()
    pass                            # HOW? - Ex: class Wizard(User)

class Archer(User):
    pass

class Wizard_Of_Oz(User):
    def __int__(self, name, power):
        self.name = name 
        self.power = power
    
    def attack(self):
        print(f'Attacking with the power of {self.power}')

class Archer_Of_Wizard(User):
    def __init__(self, name, num_of_arrows):
        self.name = name 
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'Attacking with the power of {self.num_of_arrows}')


wizard1 = Wizard()
print(wizard1)                      # O/P: <__main__.Wizard object at 0x102287490>

print(wizard1.sign_in())            # O/P: Logged in as user; None


#wizard2 = Wizard_Of_Oz('Merlin', 50)
#(wizard2.attack())

archer1 = Archer_Of_Wizard('Berling', 500)
print(archer1.attack())             # O/P: Attacking with the power of 500


