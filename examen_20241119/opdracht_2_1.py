def fac1(*, x: int) -> int:
    if x < 2:
        return 1

    result = x
    if x > 0:
        for i in range(2, x):
            result *= i

        return result
    else:
        return 0

def fac2(*, x: int) -> int:
    if x < 2:
        return 1

    result = 1
    if x > 0:
        while x > 1:
            result *= x

            x -=1

        return result
    else:
        return 0

def fac3(x:int) -> int:
    return 1 if x < 2 else x * fac3(x-1)

if __name__ == "__main__":
    assert fac1(x=0) == 1
    assert fac1(x=1) == 1
    assert fac1(x=2) == 2
    assert fac1(x=3) == 6
    assert fac1(x=4) == 24
    assert fac1(x=5) == 120
    assert fac1(x=6) == 720

    assert fac2(x=0) == 1
    assert fac2(x=1) == 1
    assert fac2(x=2) == 2
    assert fac2(x=3) == 6
    assert fac2(x=4) == 24
    assert fac2(x=5) == 120
    assert fac2(x=6) == 720

    assert fac3(x=0) == 1
    assert fac3(x=1) == 1
    assert fac3(x=2) == 2
    assert fac3(x=3) == 6
    assert fac3(x=4) == 24
    assert fac3(x=5) == 120
    assert fac3(x=6) == 720

