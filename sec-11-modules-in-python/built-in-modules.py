import random
import sys

print(random.random())

# O/P: 0.6619014610257439

# argv == argvalue

first_name = sys.argv[0]
last_name = sys.argv[1]

print(f'Hello my name is {first_name} {last_name}')


# O/P: python3 built-in-modules.py sumant renukarya
# Hello my name is built-in-modules.py sumant
