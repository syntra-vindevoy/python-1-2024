import math

def mysqrt(a: int):

    x = a - 1 if a != 1 else 1

    while True:
        y = (x + a / x) / 2
        if y == x:
            break

        x = y

    return x

def mathsqrt(a: int):
    return math.sqrt(a)

def test_square_root(amount: int):

    start_nr = 1
    sqrt_nr = 1.0

    print("a", " " * 2, "mysqrt(a)", " " * 3, "mathsqrt(a)", " " * 1,  "diff")
    print("-", " " * 2, "-" * 9, " " * 3, "-" * 11, " ", "-" * 4)
    while amount >= start_nr:

        value1 = mysqrt(a = start_nr)
        value2 = mathsqrt(a = start_nr)
        value3 = abs(value1 - value2)
        print(f"{sqrt_nr}  {value1:.10f}  {value2:.10f}  {value3:.10e}")
        start_nr += 1
        sqrt_nr += 1


def main():
    test_square_root(9)

if __name__ == "__main__":
    main()