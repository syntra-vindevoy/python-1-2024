import random
import statistics

def hoger_lager(min, max):
    x = random.randint(min, max)
    y = random.randint(min, max)
    count = 0
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
    result.append(hoger_lager(0, 10000))

print (max(result))
print (min(result))
print (statistics.mean(result))