
# function n days p month - made by GC

def dom(y, m):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m == 2:
        return is_leap(y)
    #else:
    #if m in [4,6,9,11]:
    return 30

# most efficient way to program n days p month - made by YV

def days_in_month(month :int, year :int):
    return [31, 28 + is_leap2(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] [month - 1]


# function leap_year long and unnecessary - made by GC

def is_leap(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return 29
    else:
        return 28

# function leap_year2 short and much efficient - made by YV

def is_leap2(y2):
    return y2 % 4 == 0 and y2 % 100 != 0 or y2 % 400 == 0

# Testing of the dom function

assert (dom(2024, 2) == 29)
assert (dom(1800, 2) == 28)
assert (dom(1900, 2) == 28)
assert (dom(2016, 2) == 29)
assert (dom(2000, 2) == 29)
assert (dom(1900, 2) == 28)

# Testing of the is_leap function

assert (is_leap(1900) == 28)
assert (is_leap(2024) == 29)

print(is_leap2(2021))
print(days_in_month(2, 2000))

# function for determine the days of the week - made by YV
def day_of_the_week(year :int, month :int, day :int):

    total_days = -1 # if you want to start counting form 0, you need to declare total_days = -1

    for y in range(1900, year):
        if is_leap2(y):
            total_days += 366
        else:
            total_days += 365

    for m in range(1, month):
        total_days += days_in_month(m, year)

    total_days += day

    return total_days % 7 + 1

print(day_of_the_week(1900, 1, 7))
print(day_of_the_week(2024, 10, 15))