def russian_peasant(a: int, b: int) -> int:
    if b == 0:
        return 0
    elif b % 2 != 0:
        return a + russian_peasant(a * 2, b // 2)
    else:
        return russian_peasant(a * 2, b // 2)






