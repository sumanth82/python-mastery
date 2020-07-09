#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    

# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('Jimmy', '1')
cat2 = Cat('Johnny', '1')
cat3 = Cat('Sony', '4')

print(cat1.name)    # O/P: Jimmy 

# 2 Create a function that finds the oldest cat



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2