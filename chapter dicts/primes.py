from time import perf_counter


def primes (number):
    prime_list = [2,]
    n = 3

    while len(prime_list) < number:

        prime_check = True
        for i in prime_list[1:]:
            if i * i > n: break #stops sequence at sqrt of n, no need to continue checking higher values
            if n % i == 0:
                prime_check = False
                break
        if prime_check: prime_list.append(n)
        n += 2

    return prime_list

# if __name__ == '__main__':
#     start = perf_counter()
#     n = 10000
#     primes_list = primes(n)
#     stop = perf_counter()
#     print (primes_list)
#     print (f"{len(primes_list)} primes found in {stop - start} seconds")


def primes_dict (total_numbers):
    prime_dict = {2:4,}
    n = 3

    while len(prime_dict) < total_numbers:

        prime_check = True
        for i in prime_dict:
            if prime_dict[i] > n: break
            if n % i == 0:
                prime_check = False
                break
        if prime_check: prime_dict[n] = n * n
        n += 2

    return prime_dict.keys()

# if __name__ == '__main__':
#     start = perf_counter()
#     total_numbers = 100000
#     primes = primes_dict(total_numbers)
#     stop = perf_counter()
#     print(primes)
#     print (f"{len(primes)} primes found in {stop - start} seconds")

def primes_eratosthenes(max_number):

    lijst = list(range(2, max_number+1))
    position = 0
    multiplier = 2

    while lijst[position] ** 2 < max_number:
        while lijst[position] * multiplier <= max_number:
            if lijst[position] * multiplier in lijst:
                lijst.remove(lijst[position] * multiplier)
                print (lijst)
            multiplier += 1
        multiplier = 2
        position += 1
    return lijst


if __name__ == '__main__':
    start = perf_counter()
    max_number = 20
    primes = primes_eratosthenes(max_number)
    stop = perf_counter()
    print(primes)
    print (f"{len(primes)} primes found in {stop - start} seconds")