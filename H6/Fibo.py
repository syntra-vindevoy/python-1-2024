def fibo(n: int) -> int:
    if n < 2:
        return n

    fibo_0 = 0
    fibo_1 = 1

    return fibo(n-1) + fibo(n-2)

    for _ in range(2, n + 1):
        s = fibo_0 + fibo_1
        fibo_0 = fibo_1
        fibo_1 = s

    return fibo_0 + fibo_1

assert fibo(0) == 0
assert fibo(1) == 1
assert fibo(2) == 1
assert fibo(3) == 2
assert fibo(4) == 3
assert fibo(5) == 5
assert fibo(6) == 8
assert fibo(7) == 13
assert fibo(8) == 21

