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


def fibo_tuple(n: int, first_item: int = 0, last_item: int = 1) -> (int, int):
    if n < 2:
        return first_item, last_item
    return fibo_tuple(n - 1, last_item, last_item + first_item)


def fibo(n: int = 5):
    if n == 0:
        return 0
    if n == 1:
        return 1
    _, last_item = fibo_tuple(n)
    return last_item


def fibo_list_get(length: int = 10, fibo_list=None) -> list[int]:
    fibo_list = [0, 1]
    if length <= 2:
        return fibo_list
    for i in range(length - 2):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return fibo_list


def fibo_item_get(position: int = 5):
    if position == 0:
        return 0  # fibo starts with 2 items, this corrects the problem
    return fibo_list_get(position + 1)[-1]


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


def print_function(func):
    print(func(0))
    print(func(1))
    print(func(2))
    print(func(3))
    print(func(4))
    print(func(5))
    print(func(6))
    print(func(7))
    print(func(8))


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
    assert fibo_list_get(0) == [0, 1]
    assert fibo_list_get(1) == [0, 1]
    assert fibo_list_get(2) == [0, 1]
    assert fibo_list_get(3) == [0, 1, 1]
    assert fibo_list_get(4) == [0, 1, 1, 2]
    assert fibo_list_get(5) == [0, 1, 1, 2, 3]

    assert_function(fibo)

    assert_function(fibo_item_get)
    print(fibo_item_get(0))


if __name__ == "__main__":
    main()
