import math

def is_prime1(n):
    for i in range(2, n):       #Do not include 1 and itself
        if n % i == 0:
            return False
    return True

#Only check div by 2
#In range until sqrt + 1 --> because for 21: 3x7 = 7x3 so no point in checking higher thant sqrt
#Excluded the uneven none primes from the in range --> not yet possible with what we currently saw

def is_prime(n:int) -> bool:

    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(7))
print(is_prime(9))
print(is_prime(11))
print(is_prime(13))
print(is_prime(15))
print(is_prime(17))
print(is_prime(19))
print(is_prime(23))
print(is_prime(27))

