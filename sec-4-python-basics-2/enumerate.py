# Provides an index counter for an object (Be it a list or a string):

for i, char in enumerate(['Hello', 'My', 'First', 'Name', 'is', 'Mike']):
    print(i, char)

# O/P: 0 Hello
#1 My
#2 First
#3 Name
#4 is
#5 Mike

# Exercise: Find the index of value 50 in the list below:

test_list=list(range(0, 500, 10))
print(test_list)

# O/P: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 
# 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490]

for i, char in enumerate(test_list):
    if char == 50:
        print(f'Index of 50 is: {i}')

# Index of 50 is: 5



