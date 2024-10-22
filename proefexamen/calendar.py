import date_string as ds
import dow
import dom
from proefexamen.dom import days_of_month


def print_calendar(year: int, mont: int) -> None:
    first_day_of_week = dow.day_of_the_week(year, mont, 1)
    print(f"eerste dag van de maand: dag {first_day_of_week} {ds.name_of_day(first_day_of_week)}")

    print(f'{ds.name_of_month(12)} {year}')
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

    for i in range(days_of_month(year, mont) // 7 + 1):
        print_one_line(first_day_of_week - 6, first_day_of_week + 1)
        first_day_of_week += 7


def main():
    print_calendar(2022, 12)
    # print_calendar(2022, 12)


if __name__ == "__main__":
    main()
