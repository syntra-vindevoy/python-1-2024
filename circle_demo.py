#define days of month

def dom(y,m)
    return 31

#print(dom(2024,1))  -->

assert dom(2024, 1) == 31
assert dom(2024, 2) == 29
assert dom(2000, 2) == 29
assert dom(2100, 2) == 28
assert dom(2023, 2) == 28
