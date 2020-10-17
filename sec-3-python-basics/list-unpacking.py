a,b,c = [1,2,3]

print(a)
print(b)
print(c)

# O/P: 1
#2
#3

# Now, extend this to list and use list unpacking:

a,b,c,*others,d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(others)
print(d)

# O/P: 1
#2
#3
#[4, 5, 6, 7, 8]
#9

