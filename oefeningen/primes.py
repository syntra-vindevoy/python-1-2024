from time import time


prime_dict = dict()
prime_list = list()


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(
            f"Time taken to execute {func.__name__}:{end_time - start_time:.4f} seconds"
        )
        return result

    return wrapper


def is_prime(number: int):
    number_is_prime = True
    for i in range(2, number):
        if number % i == 0:
            number_is_prime = False
            break
    return number_is_prime


def create_prime_list(length: int):
    num = 0
    while len(prime_list) < length:
        # sleep(.25)
        num += 1
        if is_prime(num):
            prime_list.append(num)
    return prime_list


assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(5) == True
assert is_prime(9) == False


@timing
def main():
    print(create_prime_list(1000))


if __name__ == "__main__":
    main()
