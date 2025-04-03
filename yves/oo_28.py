import time

from yves.tracer import trace_func


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function started at: {start}")
        print(f"Function ended at: {end}")
        print(f"Time taken: {end - start} seconds")

        return result

    return wrapper

@trace_func
def toto(a, b):
    time.sleep(1)


def main():
    toto(1, 2)


if __name__ == "__main__":
    main()