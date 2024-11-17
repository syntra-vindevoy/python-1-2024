def print_calendar(year, month):
    days = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month_days[1] = 29
    first_day = (sum(month_days[:month - 1]) + 5) % 7
    print(f"December {year}")
    print()
    print(" ".join(days))
    print("   " * first_day, end="")
    for day in range(1, month_days[month - 1] + 1):
        print(f"{day:2} ", end="")
        if (first_day + day) % 7 == 0:
            print()
    print()

print_calendar(2022, 12)