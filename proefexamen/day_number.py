from dom import *  # importing our days of month


def day_number(year: int, month: int, day: int) -> int:
    x = 0

    if month < 3:
        if month == 1:
            return x + day
        return x + 31 + day
    else:
        for m in range(1, month):
            x += days_of_month(year, m)
        x = x + day

    return x


def main():
    assert day_number(2020, 1, 1) == 1
    assert day_number(2020, 1, 15) == 15
    assert day_number(2020, 2, 1) == 32
    assert day_number(2020, 2, 15) == 46
    assert day_number(2020, 3, 1) == 61
    assert day_number(2020, 12, 31) == 366

    assert day_number(2022, 1, 1) == 1
    assert day_number(2022, 2, 1) == 32
    assert day_number(2022, 3, 1) == 60
    assert day_number(2022, 12, 31) == 365


if __name__ == "__main__":
    main()
