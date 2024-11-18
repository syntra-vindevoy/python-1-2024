def print_calendar(year):
    days = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month_days[1] = 29
    months = ["Januari", "Februari", "Maart", "April", "Mei", "Juni",
              "Juli", "Augustus", "September", "Oktober", "November", "December"]

    first_day = 5
    for month in range(12):
        print(f"{months[month]} {year}")
        print(" ".join(days))
        print("   " * first_day, end="")
        for day in range(1, month_days[month] + 1):
            print(f"{day:2} ", end="")
            if (first_day + day) % 7 == 0:
                print()
        print("\n")

        first_day = (first_day + month_days[month]) % 7

print_calendar(2022)

