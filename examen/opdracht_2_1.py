def fac_for(n):
    if n < 2:
        return 1
    result = n
    for i in range(2, n):
        result *= i
    return result

def fac_while(n):
    if n < 2:
        return 1
    result = n
    i = 2
    while i < n:
        result *= i
        i += 1
    return result

def fac_recursion(n):
    if n < 2:
        return 1
    return n * fac_recursion(n - 1)


def main():

    functions = [fac_for, fac_while, fac_recursion]
    for func in functions:
        assert func(0) == 1
        assert func(1) == 1
        assert func(2) == 2
        assert func(3) == 6
        assert func(4) == 24
        assert func(5) == 120
        assert func(6) == 720


if __name__ == "__main__":
    main()


