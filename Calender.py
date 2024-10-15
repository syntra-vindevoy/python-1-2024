specifiek_jaar = 2024

def schrikkeljaar (jaar : int):
    if jaar // 4 or jaar // 400:
        return 29
    else:
        return 28

def months (y, m):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return "31"
    if y == specifiek_jaar and m == 2:
        return "28"
    if y == specifiek_jaar and m == 2 and schrikkeljaar(y) == 29:
        return "29"
    if m == 4 or m == 6 or m == 9 or m == 11:
        return "30"

print(schrikkeljaar(2023))