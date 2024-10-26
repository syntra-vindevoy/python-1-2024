import math


def square_root(number, estimate):
    while True:
        result = (estimate + number / estimate) / 2
        if result == estimate:
            return estimate
        estimate = result
        # print(f"estimate: {estimate}")


def print_table():
    def print_header():
        column1 = "a"
        column2 = f"square_root(a,1)"
        column3 = "math.sqrt(a)"
        column4 = "diff"
        print(f"{column1:10} {column2:20} {column3:20} {column4:22}")

    def print_body():
        for i in range(1, 11):
            column1 = i
            column2 = square_root(i, 1)
            column3 = math.sqrt(i)
            column4 = abs(column2 - column3)
            print(f"{column1:10} {column2:20} {column3:20} {column4:22}")

    print_header()
    print_body()


def tests():
    assert square_root(9, 3) == 3
    assert square_root(25, 4) == 5


def main():
    tests()
    print_table()


if __name__ == "__main__":
    main()
