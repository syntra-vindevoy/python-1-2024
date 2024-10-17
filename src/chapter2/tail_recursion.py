def fact (n: int, t: int = 1) -> int:
    if n < 2:
        return t

    return fact (n - 1, n * t)


assert fact (0) == 1
assert fact (1) == 1
assert fact (2) == 2
assert fact (3) == 6
assert fact (4) == 24
assert fact (5) == 120
assert fact (6) == 720
