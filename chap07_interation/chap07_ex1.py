def mysqrt(number: float) -> float:
    x = number

    while True:
        print(x)

        y = (x + (number / x)) / 2
        if y == x:
            break

        x = y

mysqrt(120)