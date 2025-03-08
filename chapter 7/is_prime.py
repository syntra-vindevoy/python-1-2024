import math
def is_prime(n):
    #niet zo efficient
    for i in range (2, n):
        if n % i == 0:
            return False
        return True
print (is_prime (5))

#deelbaar door 2 moet maar 1 x gechecked worden
#deelbaar door 3 moet dan ook 9, 27 niet meer checken

def is_prime_2 (n):
    if n % 2 == 0:
        return False
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True
print (is_prime_2 (7871))






