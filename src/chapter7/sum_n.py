def sumer(n):
    if n == 0:
        return 0
    return n+sumer(n-1)

def optimized_sumer(n):
    return n * (n + 1) // 2

def sum_while(n):
    s=0
    while n > 0:
        s += n
        n -=1
    return s

assert optimized_sumer(5) == 1+2+3+4+5
assert optimized_sumer(0) == 0

assert optimized_sumer(5) == 1+2+3+4+5
assert optimized_sumer(0) == 0

assert sum_while(5) == 1+2+3+4+5
assert optimized_sumer(0) == 0