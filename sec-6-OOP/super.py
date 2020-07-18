#super()

# Use Case - Let's say you have 2 classes with __init__ method() defined in them; 
# To call a method in class 2, which inherits from class 1 ( (an attribute)) will not work if __init__ method is defined in both;
# 
# To resolve this, in a 2nd class where you define __init__ method, use this format - <class1_name>.__init__(self, <attribute-in-1st class>)

# Example - 1:

class User(object):
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print('logged in')

class Guest(User):
    def __init__(self, guestname, power, email):
        User.__init__(self, email) # OR use super() method
        #super().__init(email) # No need to add self with super() method
        self.guestname = guestname
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'attacking with the power of {self.power}')

wizard1 = Guest('Merlin', 60, 'merlin@gmail.com')
#print(wizard1.email)    # AttributeError: 'Guest' object has no attribute 'email'

print(wizard1.sign_in())        # logged in ; None
print(wizard1.email)            # Error - AttributeError: 'Guest' object has no attribute 'email'; This is WHAT WE WILL SOLVE;

# How to solve this Error? See Below:
# Add this in line 20 to use the email attribute defined in class 1 - User.__Init__(self, email)

# Now, after adding line 19, this is the way you get: merlin@gmail.com

# OTHER Way - use super() (it's a keyword); Refers to the class above
# Format:

#super().__init__(email)

# introspection - ability to find the type of an object at runtime (when code is running)
