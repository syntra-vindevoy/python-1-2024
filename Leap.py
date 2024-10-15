def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#int en bool doet eigelijk niks

# Leap year cases
assert is_leap_year(2020) == True, "Test Case 1 Failed: 2020 is a leap year"
assert is_leap_year(2000) == True, "Test Case 2 Failed: 2000 is a leap year (divisible by 400)"
assert is_leap_year(1600) == True, "Test Case 3 Failed: 1600 is a leap year (divisible by 400)"

# Non-leap year cases
assert is_leap_year(1900) == False, "Test Case 4 Failed: 1900 is not a leap year (divisible by 100 but not 400)"
assert is_leap_year(2021) == False, "Test Case 5 Failed: 2021 is not a leap year"
assert is_leap_year(2100) == False, "Test Case 6 Failed: 2100 is not a leap year (divisible by 100 but not 400)"

def days_in_month(month,year)
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap_year(year)
            return 29
        else:
            return 28
    return 31