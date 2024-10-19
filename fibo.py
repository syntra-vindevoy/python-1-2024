def fibo_recursion(n: int) -> int:
    if n < 2:
        return n

    fibo_0 = 0
    fibo_1 = 1

    for _ in range(2, n):
        fibo_0, fibo_1 = fibo_1, fibo_0 + fibo_1
        # print(fibo_0, fibo_1)
    return fibo_0 + fibo_1


def fibo_recursion_draft(n: int, first_item: int = 0, last_item: int = 1) -> int:
    if n == 0:
        return first_item
    if n == 1:
        return last_item
    return fibo_recursion_draft(n - 1, last_item, last_item + first_item)


def fibo_tail_recursion(n: int, a: int = 0, b: int = 1) -> int:
    if n == 0:
        return a
    if n == 1:
        return b
    return fibo_tail_recursion(n - 1, b, a + b)


def fibo_while(n: int) -> int:
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


def assert_function(func):
    assert func(0) == 0
    assert func(1) == 1
    assert func(2) == 1
    assert func(3) == 2
    assert func(4) == 3
    assert func(5) == 5
    assert func(6) == 8
    assert func(7) == 13
    assert func(8) == 21


def fibo_tuple(n: int, first_item: int = 0, last_item: int = 1) -> (int, int):
    if n < 2:
        return first_item, last_item
    return fibo_tuple(n - 1, last_item, last_item + first_item)


def fibo(n: int = 5):
    _, last_item = fibo_tuple(n)
    return last_item


def main():
    # print(fibo_recursion(8))
    assert_function(fibo_recursion)
    assert_function(fibo_tail_recursion)
    assert_function(fibo_while)
    assert_function(fibo_recursion_draft)
    assert fibo_tuple(0) == (0, 1)
    assert fibo_tuple(1) == (0, 1)
    assert fibo_tuple(2) == (1, 1)
    assert fibo_tuple(3) == (1, 2)


if __name__ == '__main__':
    main()
