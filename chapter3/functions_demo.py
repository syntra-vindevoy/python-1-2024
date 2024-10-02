def calculate_gcd (a:int, b:int) -> int:
    assert type(a) == int and type(b) == int, "Must be integers"
    while b:
        a, b = b, a % b
    return a


assert calculate_gcd (2, 3) == 1,"Oh no! This assertion failed!"
assert calculate_gcd (48, 12) == 12,"Oh no! This assertion failed!"

assert calculate_gcd (48, 2) == 2,"Oh no! This assertion failed!"

try:
    assert calculate_gcd ("48", 2) == 2,"Oh no! This assertion failed!"
except AssertionError:
    pass
