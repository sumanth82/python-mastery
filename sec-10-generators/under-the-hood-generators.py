
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break


special_for([1, 2, 3])


# O/P:

# <list_iterator object at 0x10df7a790 >
# 2
# <list_iterator object at 0x10df7a790 >
# 4
# <list_iterator object at 0x10df7a790 >
# 6
# <list_iterator object at 0x10df7a790 >
