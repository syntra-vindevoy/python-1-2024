import datetime

start = datetime.datetime.now()
def fibo(n : int) -> int:
    if n < 2:
       return n

    fibo_0 = 0
    fibo_1 = 1

    for _ in range(2, n):
        s = fibo_0 + fibo_1
        fibo_0 = fibo_1
        fibo_1 = s

        #fibo_0, fibo_1 = fibo_1, fibo_0 + fibo_1
    return fibo_0 + fibo_1


print(fibo(60))

end = datetime.datetime.now()
total = end - start
print(total)

start1 = datetime.datetime.now()
def fibo_recursive(n: int) -> int:
    if n < 2:
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)

print(fibo_recursive(40))
end1 = datetime.datetime.now()
total1 = end1 - start1
print(total1)

assert fibo(0) == 0
assert fibo(1) == 1
assert fibo(2) == 1
assert fibo(3) == 2
assert fibo(4) == 3
assert fibo(5) == 5
assert fibo(6) == 8
assert fibo(7) == 13
assert fibo(8) == 21