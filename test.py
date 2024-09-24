import math  # complete import
from datetime import datetime
from math import pi  # partial import
from math import pi as pie  # partial import with alias
import altair as alt  # complete import


def get_seconds(minutes: int, seconds: int) -> int:
    seconds_from_minutes = minutes * 60
    return seconds_from_minutes + seconds


def get_miles_from_kilometers(kilometers: float) -> float:
    return kilometers * 1.609


def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def is_leap_year_0(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def is_leap_year_1(year: int) -> bool:
    if year % 4 > 0:
        return False
    if year % 100 > 0:
        return True
    if year % 400 > 0:
        return False
    return True


def is_leap_year_2(year: int) -> bool:
    if year % 4 > 0:
        return False
    elif year % 100 > 0:
        return True
    elif year % 400 > 0:
        return False
    return True


def is_leap_year_3(year: int):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def print_pi():
    print(f"pi= {math.pi}")
    print(f"pi= {pi}")
    print(f"pi= {pie}")


def print_now():
    print(datetime.now())


def main():
    years = (2000, 2001, 2002, 2003, 2004, 2100, 2200)
    for y in years:
        print(f"year= {y}")
        print(is_leap_year(y))
        print(is_leap_year_0(y))
        print(is_leap_year_1(y))
        print(is_leap_year_2(y))
        print(is_leap_year_3(y))

    print_pi()
    print_now()


if __name__ == '__main__':
    main()
