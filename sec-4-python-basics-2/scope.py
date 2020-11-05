# variable scope;

# global scope
# function scope


# Hierarchy for function scope:

# 1. Start with local
# 2. Parent local
# 3. global
# 4. built-in Python functions

a = 1       # global scope


def confusion():
    a = 5
    return a


print(a)
print(confusion())

# O/P: 1
# 5


def parent():
    a = 10

    def confusion():
        return a
    return confusion()


print(parent())  # O/P: 10
print(a)        # O/P: 1


# global keyword

total = 0


def count():
    global total
    total += 1
    return total


print(count())  # O/P: 1


# Instead of using the global keyword, use this dependency injection:

totale = 0


def count(totale):
    totale += 1
    return totale


print(count(totale))  # O/P: 1

print(count(count(count(totale))))  # O/P: 3


# nonlocal keyword - Used to represent a parent variable but NOT a global variable:


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner: ", x)

    inner()
    print("outer: ", x)


outer()

# O/P:

# inner:  nonlocal
# outer:  nonlocal

# Essentially with nonlocal keyword, you set the value for the variable NOT just in the local but also in the parent;
