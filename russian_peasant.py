#The recursion version
def russian_peasant(a: int, b:int) -> int:
    if b == 0:
        return 0
    elif b % 2 != 0:
        return a + russian_peasant(a * 2, b // 2)
    else:
        return russian_peasant(a * 2, b // 2)

def test_russian_peasant():
    #small number
    assert russian_peasant(1, 1) == 1
    assert russian_peasant(2, 2) == 4
    assert russian_peasant(3, 3) == 9

    #large numbers
    assert russian_peasant(43, 456) == 43 * 456
    assert russian_peasant(67, 456) == 67 * 456

    #specials and very large numbers
    a = 12**9
    b = 12**9
    assert russian_peasant(a, b) == a * b


