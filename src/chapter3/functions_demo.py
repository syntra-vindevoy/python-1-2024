def calculate_gcd (a:int, b:int) -> int:
    """
    Calculate the greatest common divisor of a and b
    Args:
        a (object):
        b (object):
    Returns:int
    """
    assert type(a) == int and type(b) == int, "Must be integers"
    while b:
        a, b = b, a % b
    return a

def calculate_gcd_alt(a, b):
    if b == 0:  # Base case: if b is 0, gcd is a
        return a
    else:
        return calculate_gcd(b, a % b)

assert calculate_gcd (2, 3) == 1,"Oh no! This assertion failed!"
assert calculate_gcd (48, 12) == 12,"Oh no! This assertion failed!"

assert calculate_gcd (48, 2) == 2,"Oh no! This assertion failed!"

try:
    assert calculate_gcd ("48", 2) == 2,"Oh no! This assertion failed!"
except AssertionError:
    pass
