def schrikkeljaar (jaar : int):
    if jaar / 4 == int or jaar / 400 == int:
        return 29
    else:
        return 28

def months (y, m):
    if y == 2024 and m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return "31"
    if y == 2024 and m == 2:
        return "28"
    if y == 2024 and m == 4 or m == 6 or m == 9 or m == 11:
        return "30"

# print (months(2024, 1))
# print (months(2024, 2))
# print (f'{2024 % 400 == int}')
# print (f'{2024 % 400 == float}')
print (schrikkeljaar(2024))
print (schrikkeljaar(1900))
print (schrikkeljaar(2000))