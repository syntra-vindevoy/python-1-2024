from proefexamen.dom import days_of_month


def day_number(year: int, month: int, day: int) -> int:
    x = 0

    if month < 3:
        if month == 1:
            return x + day
        return x + 31 + day
    else:
        for m in range(1, month):
            x = x + days_of_month(year, m)
            print(m)
            print(x)
        y = x + day
        print(y)

    return x

day_number(2020, 3, 1)

#for m in range(1, month + 1):
    #return x + days_of_month(year, m)