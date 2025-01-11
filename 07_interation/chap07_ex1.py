def mysqrt(number: float) -> float:
    x = number

    while True:
        print(x)

        y = (x + (number / x)) / 2
        if y == x:
            break

        x = y

mysqrt(120)




def mysqrt(number: float, tolerance: float = 1e-10) -> float:
    x = number

    while True:
        y = (x + (number / x)) / 2
        if abs(y - x) < tolerance:  # Compare with a small tolerance
            return y
        x = y