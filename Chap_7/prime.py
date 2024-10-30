def sieve_of_eratosthenes(limit):
    """Return a list of all primes up to the given limit using the Sieve of Eratosthenes with while loop."""
    if limit <= 1:
        return []

    # Initialize the sieve list with True values
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    num = 2
    while num * num <= limit:
        if sieve[num]:
            # Mark multiples of num as False
            multiple = num * num
            while multiple <= limit:
                sieve[multiple] = False
                multiple += num
        num += 1

    # Extract prime numbers from sieve
    primes = []
    for i in range(limit + 1):
        if sieve[i]:
            primes.append(i)

    return primes


def print_primes(primes):
    for i, num in enumerate(primes):
        # Print numbers in row with maximum 10 numbers
        print(f"{num:7}", end=' ')
        if (i + 1) % 10 == 0:
            print()
    if len(primes) % 10 != 0:
        print()


# Example Usage
limit = 100
primes = sieve_of_eratosthenes(limit)
print(f"Prime numbers up to {limit} are:")
print_primes(primes)
