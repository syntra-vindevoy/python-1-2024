from dom import days_of_month  # importing our days of month

# def day_number(year: int, month: int, day: int) -> int:
#     day_of_year = sum(days_of_month[year, :month - 1]) + day
#     return day_of_year

def day_number(year: int, month: int, day: int) -> int:
    total_days = 0
    for m in range(1, month):
        total_days += days_of_month(year, m)

    total_days += day

    return total_days

def main():
    assert day_number(2024, 1, 1) == 1
    assert day_number(2024, 1, 30) == 30
    assert day_number(2024, 2, 1) == 32
    assert day_number(2024, 3, 1) == 61
    assert day_number(2024, 12, 31) == 366

    assert day_number(2026, 1, 1) == 1
    assert day_number(2026, 2, 1) == 32
    assert day_number(2026, 3, 1) == 60
    assert day_number(2026, 12, 31) == 365


if __name__ == "__main__":
    main()
