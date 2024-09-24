import math                         #Import the complete Math Library
print(math.pi)


from math import pi                 #Only Load a specific part of the Math Library
print(pi)


import datetime
print(datetime.datetime.now())


from datetime import datetime
print(datetime.now())

n = 17
print("De waarde van n is: " + str(n))
print("De waarde van n is:", n)
print(f"De waarde van n is: {n}")               #f-string = formated string --> preferred way
print(f"De waarde van n is: {n * 2}")
