def week_number(year: int, month: int, day: int):
    pass


def main():
    assert week_number(2022, 1, 1) == 1
    assert week_number(2022, 1, 8) == 2
    assert week_number(2022, 1, 15) == 3
    assert week_number(2022, 1, 25) == 4
    assert week_number(2022, 1, 30) == 5
if __name__ == "__main__":
    main()
