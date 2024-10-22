from dom import days_of_month  # importing our days of month

def days_in_year(year: int) -> int:
    total_days = 0
    for month in range(1, 13):  # Loop through all months (1 to 12)
        total_days += days_of_month(year, month)  # Add the days of each month
    return total_days

def day_number(year: int, month: int, day: int) -> int:
    if month < 1 or month > 12:
        raise ValueError("Maand moet tussen 1 en 12 liggen.")
    if day < 1 or day > days_of_month(year, month):
        raise ValueError(f"Dag moet tussen 1 en {days_of_month(year, month)} liggen voor maand {month}.")

    totaal_dagen = 0

    # Tel de dagen in de maanden vóór de gegeven maand
    for m in range(1, month):
        totaal_dagen += days_of_month(year, m)

    # Voeg de dagen van de huidige maand toe
    totaal_dagen += day

    return totaal_dagen

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
