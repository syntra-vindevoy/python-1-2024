def dow (year, month, day):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    v = round ((year + year / 4 - year / 100 + year / 400 + t[month - 1] + day) % 7)
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[v]


assert dow (2024, 10, 15) == "Tuesday"
