# How to find something is an instance of a class? 
# ANS: isinstance - A built-in function 
# isinstance(instance, class)

# Everything in Python inherits from the - object base class.

# So the below class User(), under the hood takes - class User(object) as it's parent class. 

class User():
    def sign_in(self):
        print('logged in')


user_signin = User()
user_signin.sign_in()

print(isinstance(user_signin, User))    # O/P: True



