# Custom Class created here that behaves like a range function - This essentially uses generators to achieve this - next()

class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)

for i in gen:
    print(i)


# O/P: 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# .
# .
# .
# .
# .
# 91
# 92
# 93
# 94
# 95
# 96
# 97
# 98
# 99
