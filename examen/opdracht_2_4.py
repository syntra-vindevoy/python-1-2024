# Russian peasant multiplication
def russian_peasant_recursion(a: int, b: int) -> int:
    if b == 0:
        return 0
    elif b % 2 != 0:
        return a + russian_peasant_recursion(a * 2, b // 2)
    else:
        return russian_peasant_recursion(a * 2, b // 2)

def russian_peasant_while(a: int, b: int) -> int:
    result = 0
    while b > 0:
        if b % 2 != 0:
            result += a
        a *= 2
        b //= 2
    return result


def main():


    assert russian_peasant_recursion(1, 1) == 1
    assert russian_peasant_recursion(1, 2) == 2
    assert russian_peasant_recursion(2, 2) == 4
    assert russian_peasant_recursion(3, 3) == 9
    assert russian_peasant_recursion(999, 9999) == 999*9999
    assert russian_peasant_recursion(1, 20) == 20
    assert russian_peasant_recursion(5, 7) == 35
    assert russian_peasant_recursion(3, 4) == 12
    assert russian_peasant_recursion(0, 0) == 0
    assert russian_peasant_recursion(1000000000, 99999999) == 1000000000*99999999

    assert russian_peasant_while(1, 1) == 1
    assert russian_peasant_while(1, 2) == 2
    assert russian_peasant_while(2, 2) == 4
    assert russian_peasant_while(3, 3) == 9
    assert russian_peasant_while(999, 9999) == 999*9999
    assert russian_peasant_while(1, 20) == 20
    assert russian_peasant_while(5, 7) == 35
    assert russian_peasant_while(3, 4) == 12
    assert russian_peasant_while(0, 0) == 0
    assert russian_peasant_while(1000000000, 99999999) == 1000000000*99999999