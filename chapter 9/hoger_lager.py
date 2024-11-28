
import random

def hoger_lager():
    x = random.randint(0, 10000)
    y = random.randint(0, 10000)
    count = 0
    min = 0
    max = 10000
    print (x,y)
    while x != y:
        print (y)
        count += 1
        if y > x:
            max = y
            print ("lager")
            y = random.randint(min, max)
        elif y < x:
            min = y
            print ("hoger")
            y = random.randint(min, max)
    print (f"Het heeft {count} beurten geduurd")
hoger_lager()
