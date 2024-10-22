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
