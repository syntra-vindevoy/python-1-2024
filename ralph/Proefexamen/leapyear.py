def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    # Not dividable by 4
    assert is_leap_year(2021) is False

    # Dividable by 4, not by 100
    assert is_leap_year(2020) is True

    # Dividable by 100, not by 400
    assert is_leap_year(2100) is False

    # Dividable by 100 and 400
    assert is_leap_year(2000) is True

if __name__ == "__main__":
    main()
