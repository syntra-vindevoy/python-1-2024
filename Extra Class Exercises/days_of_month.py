# def days of month: def dom(year, month):  Geef het aantal dagen in een maand
# def is_leap(year): -- is een bepaald jaar een schrikkeljaar of niet?


#defines leap year and returns True or False
#Code below can be rewritten to read quicker:
#return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): (this returns True or False just like below)
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

#Asserts to test function is_leap(year)
assert is_leap(2024) == True
assert is_leap(2100) == False
assert is_leap(1996) == True
assert is_leap(1) == False


#function to return number of days in a month and checking for leap year
def dom(year: int, month: int) -> bool:
    #also easier: if month in [1, 3, 5, 7, 8, 10, 12]:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        if is_leap(year):
            return 29
        else:
            return 28
    else:
        return 30



if __name__ == "__main__":
    #asserts to test dom function
    assert dom(2024, 2) == 29  # Leap year
    assert dom(2023, 2) == 28  # Non-leap year
    assert dom(2023, 4) == 30  # April has 30 days
    assert dom(2023, 7) == 31  # July has 31 days

    print(dom(2076, 2))