from functools import reduce

# lambda with reduce

numbers = [1,2,3,4,5]
product = reduce(lambda x,y: x*y, numbers)