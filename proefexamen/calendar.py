import date_string as ds
import dow
import dom
from proefexamen.dom import days_of_month


def print_calendar(year: int, mont: int) -> None:
    first_day_of_week = dow.day_of_the_week(year, mont, 1)
    # print(f"eerste dag van de maand: dag {first_day_of_week} {ds.name_of_day(first_day_of_week)}")

    print(f'\n{ds.name_of_month(mont)} {year}')
    print()
    for i in range(1, 8):
        print(ds.name_of_day(i), end=' ')
    print()

    def print_one_line(start: int, end: int):
        for i in range(start, end):
            if i < 1:
                print('  ', end=' ')
            elif i > dom.days_of_month(year, mont):
                print(f'  ', end=' ')
            else:
                print(f'{i:2}', end=' ')

        print()

    weeks_in_month = 6
    start = 1 - first_day_of_week + 1
    for i in range(weeks_in_month):
        # print_one_line(0, 7)
        print_one_line(start, start + 7)
        start += 7


def main():
    print_calendar(2022, 10)
    print_calendar(2022, 11)
    print_calendar(2022, 12)


if __name__ == "__main__":
    main()
