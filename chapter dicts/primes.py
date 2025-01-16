from time import perf_counter

def primes (number):
    prime_list = [2,3,5,]
    n = 7

    while len(prime_list) < number:

        prime_check = True
        for i in prime_list[1:]:
            if i * i > n: break #stops sequence at sqrt of n, no need to continue checking higher values
            if n % i == 0:
                prime_check = False
                break
        if prime_check: prime_list.append(n)
        n += 2
        while n % 5 == 0 or n % 3 == 0:
            n += 2


    return prime_list

if __name__ == '__main__':
    start = perf_counter()
    n = 10000
    primes_list = primes(n)
    print (primes_list)
    stop = perf_counter()
    print (f"{len(primes_list)} primes found in {stop - start} seconds")