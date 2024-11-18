# This import is allowed as it's our own function we wrote in leapyear.py
from leapyear import *


def days_of_month(year: int , month: int) -> int:
    # January == 1 !
    if month > 12:
        raise SyntaxError('invalid month')
    return [0, 31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month]

print (days_of_month(2020, 5))
def main():
    # Leap year
    assert days_of_month(2020, 1) == 31  # Jan
    assert days_of_month(2020, 2) == 29  # Feb
    assert days_of_month(2020, 3) == 31  # Mar
    assert days_of_month(2020, 4) == 30  # Apr
    assert days_of_month(2020, 5) == 31  # May
    assert days_of_month(2020, 6) == 30  # Jun
    assert days_of_month(2020, 7) == 31  # Jul
    assert days_of_month(2020, 8) == 31  # Aug
    assert days_of_month(2020, 9) == 30  # Sep
    assert days_of_month(2020, 10) == 31  # Oct
    assert days_of_month(2020, 11) == 30  # Nov
    assert days_of_month(2020, 12) == 31  # Dec

    # No leap year
    assert days_of_month(2022, 1) == 31
    assert days_of_month(2022, 2) == 28
    assert days_of_month(2022, 3) == 31
    assert days_of_month(2022, 4) == 30
    assert days_of_month(2022, 5) == 31
    assert days_of_month(2022, 6) == 30
    assert days_of_month(2022, 7) == 31
    assert days_of_month(2022, 8) == 31
    assert days_of_month(2022, 9) == 30
    assert days_of_month(2022, 10) == 31
    assert days_of_month(2022, 11) == 30
    assert days_of_month(2022, 12) == 31


if __name__ == "__main__":
    main()
