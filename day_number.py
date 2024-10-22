from dom import days_of_month  # Importeren van de functie days_of_month

def day_number(year: int, month: int, day: int) -> int:
    """Berekent het aantal dagen sinds 1 januari van het opgegeven jaar tot de opgegeven datum."""
    total_days = 0

    # Tel het aantal dagen in de maanden van het huidige jaar tot de opgegeven maand
    for m in range(1, month):
        total_days += days_of_month(year, m)

    # Voeg de dagen in de huidige maand toe
    total_days += day

    return total_days


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
