from shopping.more_shopping.shopping_cart import buy
import utility
print(__name__)

# O/P: __main__

# FORMAT 1

#import shopping.more_shopping.shopping_cart

# print(shopping.more_shopping.shopping_cart.buy('samsung'))

# O/P: ['samsung']

# This above format is clumsy

# FORMAT 2:

# Instead use the below import format and then print

print(buy('sony'))

# O/P: ['sony']
