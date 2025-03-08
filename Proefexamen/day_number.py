from dom import days_of_month  # importing our days of month


def day_number(year: int, month: int, day: int) -> int:
    days = day #zet day al meteen bij days ipv die achteraf pas toe te voegen
    for i in range (1, month):
        days += days_of_month(month = i, year = year)

    return days

def main():
    assert day_number(2020, 1, 1) == 1
    assert day_number(2020, 2, 1) == 32
    assert day_number(2020, 3, 1) == 61
    assert day_number(2020, 12, 31) == 366

    assert day_number(2022, 1, 1) == 1
    assert day_number(2022, 2, 1) == 32
    assert day_number(2022, 3, 1) == 60
    assert day_number(2022, 12, 31) == 365


if __name__ == "__main__":
    main()
