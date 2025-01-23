from datetime import datetime


def generate_primes_sieve_no_imports(limit):
    """
    Generate the first `limit` primes using the Sieve of Eratosthenes without imports.
    """
    # Use a rough estimate for how far to search, since the n-th prime is approximately n * log(n)
    # This ensures sufficient room to find the first `limit` primes without mathematical imports.
    upper_bound = limit * 15  # Simple fallback estimate for the size of the search space

    # Boolean array for marking primes, initially assume all numbers are prime
    sieve = [True] * (upper_bound + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime

    # Implement the Sieve of Eratosthenes
    for num in range(2, int(upper_bound ** 0.5) + 1):
        if sieve[num]:  # If `num` is prime
            # Mark multiples of `num` starting from num^2
            for multiple in range(num * num, upper_bound + 1, num):
                sieve[multiple] = False


    # Extract prime numbers from the sieve
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Return only the first `limit` primes
    return primes[:limit]

if __name__ == "__main__":
# Generate the first 1000 prime numbers
    start = datetime.now()
    first_thousand_primes = generate_primes_sieve_no_imports(1000)
    print(first_thousand_primes)
    end = datetime.now()
    print("Time taken:", end - start)
# Read the list of words
