
#optie 1
def is_schrikkeljaar(year):
    """Bepaal of een jaar een schrikkeljaar is."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def dagen_in_maand(month, year):
    """Bepaal het aantal dagen in een maand van een bepaald jaar."""
    dagen_per_maand = [31, 28 + is_schrikkeljaar(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dagen_per_maand[month - 1] if 1 <= month <= 12 else 0  # Ongeldige maand

def eerste_dag_van_jaar(year):
    """Bepaal de eerste dag van het jaar (0=Zondag, 1=Maandag, etc.)."""
    if year < 1:
        return -1  # Ongeldig jaar
    q = 1
    m = 1
    if m < 3:
        m += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (q + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) - 2 * j) % 7
    return (h + 5) % 7  # Omzetten naar maandag als eerste dag

def eerste_dag_van_maand(month, year):
    """Bepaal de eerste dag van de maand."""
    eerste_dag_jan = eerste_dag_van_jaar(year)
    dagen_totale = sum(dagen_in_maand(m, year) for m in range(1, month))
    return (eerste_dag_jan + dagen_totale) % 7

def print_kalender(month, year):
    """Print de kalender voor een specifieke maand en jaar."""
    dagen = ["Ma", "Din", "Woe", "Don", "Vri", "Zat", "Zon"]
    print(f"\nKalender voor {month}/{year}")
    print(" ".join(dagen))

    eerste_dag = eerste_dag_van_maand(month, year)
    dagen_in_huidige_maand = dagen_in_maand(month, year)

    # Lege spaties voor de eerste dag
    print("   " * eerste_dag, end="")

    for dag in range(1, dagen_in_huidige_maand + 1):
        print(f"{dag:2}", end="  ")
        if (eerste_dag + dag) % 7 == 0:
            print()  # Nieuwe regel na zondag

# Vraag gebruiker om maand en jaar in te voeren
jaar = int(input("Voer het jaar in (bijv. 2023): "))
maand = int(input("Voer de maand in (1-12): "))

print_kalender(maand, jaar)




