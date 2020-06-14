import utility
import shopping.shopping_cart as shop
from shopping.shopping_cart import buy
import random

def multiply2(item):
    return item ** 2

if __name__ == '__main__':
    print('changes made')

else:
    print(__name__)
    print(buy('shoes'))
    print(utility.multiply2(25))

print(utility.multiply2(10))
print(random.randint(1,100))

