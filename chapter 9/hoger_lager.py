import random
import statistics

# def hoger_lager(min, max):
#     x = random.randint(min, max)
#     y = random.randint(min, max)
#     count = 1
#     while x != y:
#         print (f"probeer: {y}")
#         count += 1
#         if y > x:
#             max = y
#             print ("lager!")
#         else:
#             min = y
#             print ("hoger!")
#         y = random.randint(min, max)
#     print (f"Het heeft {count} beurten geduurd om {x} te vinden")
#     return count
# hoger_lager(0, 10000)
#
#
# result = []
# for i in range(1000):
#     result.append(hoger_lager(0, 10000))
#
# print (max(result))
# print (min(result))
# print (statistics.mean(result))


def hoger_lager(min, max):
    x = random.randint(min, max)
    y = (min + max) // 2 #universeler dan max // 2
    count = 1
    min_next = min
    max_next = max

    while x != y:
        #print(f"poging {count}: probeer: {y}")
        if y > x:
            #print("lager!")
            max_next = y
        else:
            #print("hoger!")
            min_next = y + 1
            #if y % 2 != 0: # doet er enkel +1 bij bij oneven getallen, maakt geen verschil in uitkomst
            #    min_next = y + 1
            #else: min_next = y
        y = (min_next + max_next) // 2
        count += 1

    #print(f"Het heeft {count} beurten geduurd om {x} te vinden")
    return count

hoger_lager(0, 10000)

result = []
for i in range(10000):
    result.append(hoger_lager(0, 10000))

print (max(result))
print (min(result))
print (statistics.mean(result))

