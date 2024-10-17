def is_schrikkeljaar(jaar):
    if (jaar % 4 == 0 and jaar % 100 != 0) or (jaar % 400 == 0):
        return True
    return False

def dagen_in_maand(jaar, maand):
    if maand == 2:
        return 29 if is_schrikkeljaar(jaar) else 28
    elif maand in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def startdag_van_maand(jaar, maand):
    if maand < 3:
        maand += 12
        jaar -= 1
    q = 1  # Eerste dag van de maand
    k = jaar % 100
    j = jaar // 100
    h = (q + 13 * (maand + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    return (h + 5) % 7

def print_kalender(jaar, maand):
    dagen_van_de_week = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]
    dagen_in_deze_maand = dagen_in_maand(jaar, maand)
    startdag = startdag_van_maand(jaar, maand)

    print(f"Kalender voor {jaar}, maand {maand}:")
    print(" ".join(dagen_van_de_week))

    print("   " * startdag, end="")

    for dag in range(1, dagen_in_deze_maand + 1):
        print(f"{dag:2}", end=" ")
        if (startdag + dag) % 7 == 0:
            print()

    print()

jaar = 2024
maand = 10
print_kalender(jaar, maand)
