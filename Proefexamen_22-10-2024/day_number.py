from leapyear import is_leap_year
from dom import days_of_month  # importing our days of month


def day_number(year: int, month: int, day: int) -> int:
    total_days = 0

    # Tel alle dagen van volledige jaren tot het opgegeven jaar
    for y in range(2020, year):
        if is_leap_year(y):
            total_days += 366  # Schrikkeljaar
        else:
            total_days += 365  # Geen schrikkeljaar

    # Tel alle dagen van volledige maanden in het opgegeven jaar tot de opgegeven maand
    for m in range(1, month):
        total_days += days_of_month(year, month)

    # Voeg de dagen van de huidige maand toe
    total_days += day

    return total_days

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
