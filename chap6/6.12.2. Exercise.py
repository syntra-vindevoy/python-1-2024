# Use incremental development to write a function called hypot that returns the length of the hypotenuse of a right triangle given
# the lengths of the other two legs as arguments.
# Note: There’s a function in the math module called hypot that does the same thing, but you should not use it for this exercise!
# Even if you can write the function correctly on the first try, start with a function that always returns 0 and practice making small changes, testing as you go.
# When you are done, the function should only return a value – it should not display anything.

import math

def hypot(a , b):

    return math.sqrt(a**2 + b**2)

print(hypot(1 , 2))