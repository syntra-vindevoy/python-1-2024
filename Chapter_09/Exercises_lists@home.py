# exercise 10.1 from book thinkpython
from random import random
from string import ascii_lowercase


t= [[1,2], [4,5,6], [3]]
def nested_sum(list):
    return sum(sum(sublist) for sublist in list)

print(nested_sum(t))
print (t[2])

# exercise 10.2 from book thinkpython V2

t2 = [1,2,3]
def cumsum(list2):
    result = []
    current_sum = 0
    for num in list2:
        current_sum += num
        result.append(current_sum)
    return result
print(cumsum(t2))

# exercise 10.3 from book thinkpython V2

t3 = [1, 2, 3, 4]
def middle(list3):
    return list3 [1:-1]
print(middle(t3))

#exercise 10.4 from book thinkpython V2 + tests with random import
from string import hexdigits
import random # ctrl + b om naar de library te gaan
t4 = [1, 2, 3, 2]
def chop(list4):
    del list4 [0:-1]
    return list4
print (chop(t4))
print(random.choice(hexdigits))

#exercise 10.5 from book thinkpython V2
t5 = [8, 1, 3, 2]
def is_sorted(list5):
    sort = sorted(list5)
    nsort = not sorted(list5)
    if list5 == sort:
        return True
    elif list5 == nsort:
        return False

print (is_sorted(t5))

