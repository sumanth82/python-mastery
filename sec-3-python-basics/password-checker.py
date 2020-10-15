name = input('Enter the username: ')
password = input('Enter the password in opaque format: ')

hidden_password = '*' * len(password)

print(f'User {name} has the password {hidden_password} and it\'s lenght is {len(password)}')
