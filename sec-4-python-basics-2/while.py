# Note: To get out of a while loop, use - break


i = 0

while (i < 50):
    print(i)
    i += 1
else:
    print('Done printing 50')

## Great use-case:

while True:
    name = input('Enter your name: ')
    if name == 'Sumant':
        break

print(name)

#Enter your name: sam - Keeps continuing; 
#Enter your name: Sumant
#Sumant


