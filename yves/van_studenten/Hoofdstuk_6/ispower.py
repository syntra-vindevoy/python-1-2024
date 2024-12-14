import math

def is_power(a, b):
    y = math.log(a, b)
    return (b ** y) == a

assert is_power(9, 3)
assert not is_power(12, 2)

