# How to find something is an instance of a class? 
# ANS: isinstance - A built-in function 
# isinstance(instance, class)


class User():
    def sign_in(self):
        print('logged in')


user_signin = User('Merlin')

user_signin.sign_in()

print(isinstance(user_signin, User))

