def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

is_leap(2024)

def days_of_month(year, month):
    list31 = (1, 3, 5, 7, 8, 10, 12)
    list30 = (4, 6, 9, 11)
    if month in list31:
        return 31
    if month in list30:
        return 30


if __name__ == "__main__":
    assert is_leap(2024) == True, "test failed"

print(days_of_month(2024, 6))


