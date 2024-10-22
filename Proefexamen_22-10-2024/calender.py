from leapyear import is_leap_year  # Zorg ervoor dat je deze functie hebt geïmporteerd


def days_of_month(year: int, month: int) -> int:
    # Controleer of de maand geldig is
    if month < 1 or month > 12:
        raise ValueError("Invalid month. Month must be between 1 and 12.")

    # Aantal dagen per maand
    if month in [4, 6, 9, 11]:  # April, Juni, September, November
        return 30
    elif month == 2:  # Februari
        return 29 if is_leap_year(year) else 28
    else:  # Januari, Maart, Mei, Juli, Augustus, Oktober, December
        return 31


def print_calendar(year: int):
    print(f"Kalender voor het jaar {year}\n")

    # Lijst van maandnamen
    months = [
        "Januari", "Februari", "Maart", "April", "Mei", "Juni",
        "Juli", "Augustus", "September", "Oktober", "November", "December"
    ]

    for month in range(1, 13):
        print(f"{months[month - 1]} {year}".center(20, ' '))
        print("Mo Tu We Th Fr Sa Su")

        # Bepaal de startdag van de maand
        first_day = week_number(year, month, 1)  # Voeg deze functie toe als je dat nog niet hebt gedaan
        total_days = days_of_month(year, month)

        # Print lege spaties voor de eerste weekdag van de maand
        print("   " * (first_day - 1), end='')

        # Print de dagen van de maand
        for day in range(1, total_days + 1):
            print(f"{day:2}", end=' ')
            if (day + first_day - 1) % 7 == 0:  # Nieuwe regel na zaterdag
                print()
        print("\n")  # Nieuwe regel na elke maand


def week_number(year: int, month: int, day: int) -> int:
    total_days = 0

    # Tel alle dagen van volledige jaren tot het opgegeven jaar
    for y in range(1900, year):
        if is_leap_year(y):
            total_days += 366  # Schrikkeljaar
        else:
            total_days += 365  # Geen schrikkeljaar

    # Tel alle dagen van volledige maanden in het opgegeven jaar tot de opgegeven maand
    for m in range(1, month):
        total_days += days_of_month(year, m)

    # Voeg de dagen van de huidige maand toe
    total_days += day

    # Bepaal de weekdag (1 = maandag, 7 = zondag)
    return (total_days % 7) + 1


def main():
    print_calendar(2022)


if __name__ == "__main__":
    main()
