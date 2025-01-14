def primes (number):
    prime_list = [2,3,5,7,]
    n = 11
    while len(prime_list) < number:
        prime_check = True
        for i in prime_list[3:]:
            if n % i == 0:
                prime_check = False
                break
        if prime_check: prime_list.append(n)
        n += 2
        while n % 5 == 0 or n % 3 == 0: n += 2
    return prime_list

print (primes(1000))