def sqrt (n):
    y = n
    x = y / 2
    for i in range (100):
        y =(x + n/x) / 2
        x = y
    return x

assert sqrt (16) == 4
assert sqrt (100) == 10
assert sqrt (3025) == 55




