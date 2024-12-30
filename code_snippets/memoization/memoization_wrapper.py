
# https://www.youtube.com/watch?v=qORqpMg3Uew

from functools import wraps
from time import time, perf_counter
import sys

def memoize(func):
    cache = {}


    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    sys.setrecursionlimit(10_000)
    start = perf_counter()
    f = fibonacci(35)
    end = perf_counter()

    print (f)
    print (f'time: {end-start} seconds')