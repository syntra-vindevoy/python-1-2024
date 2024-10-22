from leapyear import *

def days_of_month(year: int, month: int) -> int:
    odd_months = {1, 3, 5, 7, 8, 10, 12}

    if month in odd_months:
        def day_of_the_week(year: int, month: int, day: int) -> int:
            """
            Bepaalt de dag van de week voor een gegeven datum.

            Deze functie is een aangepaste versie van de originele functie van onze Japanse vriend.
            In deze versie wordt maandag beschouwd als dag 1 van de week en zondag als dag 7.

            Args:
                year (int): Het jaar van de datum (bijvoorbeeld 2022).
                month (int): De maand van de datum (1-12).
                day (int): De dag van de maand (1-31).

            Returns:
                int: Een geheel getal dat de dag van de week vertegenwoordigt,
                     waarbij maandag = 1 en zondag = 7.
            """
            offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
            year -= month < 3
            dow = (year + year // 4 - year // 100 + year // 400 + offset[month - 1] + day) % 7

            if dow == 0:
                dow = 7

            return dow

        return 31
    elif month == 2 and is_leap_year(year):
        return 29
    elif month == 2:
        return 28
    else:
        return 30

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
