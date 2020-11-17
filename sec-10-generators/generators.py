# iterable
# iterators
# generators - Ex: range()


# Let's create a custom generator - generator is always a function()
# generator functions use a keyword - yield instead of return

# Within a function, yield pauses the function and comes back to it when we do something to the function, called next


def generator_function(num):
    for i in range(num):
        yield i


g = generator_function(20)
print(g)

# O/P: <generator object generator_function at 0x1059bc450>

next(g)

next(g)

print(next(g))
print(next(g))

# O/P:
# 2
# 3
