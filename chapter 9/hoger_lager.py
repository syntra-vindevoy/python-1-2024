import random
import statistics
"""
def hoger_lager(min, max):
    x = random.randint(min, max)
    y = random.randint(min, max)
    count = 1
    while x != y:
        print (f"probeer: {y}")
        count += 1
        if y > x:
            max = y
            print ("lager!")
        else:
            min = y
            print ("hoger!")
        y = random.randint(min, max)
    print (f"Het heeft {count} beurten geduurd om {x} te vinden")
    return count
hoger_lager(0, 10000)


result = []
for i in range(1000):
    result.append(hoger_lager(0, 1000))

print (max(result))
print (min(result))
print (statistics.mean(result))"""

import random

def hoger_lager(min, max):
    x = random.randint(min, max)
    y = (min + max) // 2 #universeler dan max // 2
    count = 1
    min_next = min
    max_next = max

    while x != y:
        print(f"probeer: {y}")
        if y > x:
            print("lager!")
            max_next = y - 1  # -1 voor afronding op te vangen
        else:
            print("hoger!")
            min_next = y + 1  # +1 voor afronding op te vangen

        y = (min_next + max_next) // 2
        count += 1

    print(f"Het heeft {count} beurten geduurd om {x} te vinden")
    return count

hoger_lager(0, 10000)

result = []
for i in range(100000):
    result.append(hoger_lager(0, 10000))

print (max(result))
print (min(result))
print (statistics.mean(result))


