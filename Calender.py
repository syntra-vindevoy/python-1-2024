
def schrikkeljaar (jaar : int):
    if jaar % 4 == 0 and jaar % 100 != 0 or jaar % 400 == 0:
        return 29
    else:
        return 28

def months (y, m):
    if m == [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m == 2 and schrikkeljaar(y) == 28:
        return 28
    elif m == 2 and schrikkeljaar(y) == 29:
        return 29
    elif m == [4, 6, 9, 11]:
        return 30

#def monday_start():


def kalender (y, m):
    if months(y, m) == 28:
        for i in range (1, 32):
            print(i)

print(months(2024, 2))
print(kalender(2024, 2))
