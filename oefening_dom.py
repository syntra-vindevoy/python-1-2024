def dom(y, m):
    if m in [1,3,5,7,8,10,12]:
        return 31
    if m in [4,6,9,11]:
        return 30
    if m == 2:
        return is_leap(y)

def is_leap(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return 29
    else:
        return 28

assert (dom(2024, 2) == 29)
assert (dom(1800, 2) == 28)
assert (dom(1900, 2) == 28)
assert (dom(2016, 2) == 29)
assert (dom(2000, 2) == 29)
assert (dom(1900, 2) == 28)