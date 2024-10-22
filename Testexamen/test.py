from dom import days_of_month  # importing our days of month

def days_in_year(year: int) -> int:
    total_days = 0
    for month in range(1, 13):  # Loop through all months (1 to 12)
        total_days += days_of_month(year, month)  # Add the days of each month
    return total_days

print(days_in_year(2024))
