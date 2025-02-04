def is_power(a, b):
    if a == b:
        return True

    if a % b != 0:
        return False

    return is_power(a / b, b)


assert is_power(9, 3)
assert not is_power(9, 2)
assert is_power(27, 3)
