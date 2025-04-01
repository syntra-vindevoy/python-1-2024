import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        print(f"Function '{func.__name__}' started at: {time.ctime(start_time)}")

        result = func(*args, **kwargs)  # Execute the wrapped function

        end_time = time.time()  # Record the end time
        print(f"Function '{func.__name__}' ended at: {time.ctime(end_time)}")

        # Calculate and print the total time taken
        time_taken = end_time - start_time
        print(f"Function '{func.__name__}' took {time_taken:.4f} seconds to execute.")

        return result  # Return the wrapped function's output

    return wrapper


@measure_time
def toto(a, b):
    time.sleep(1)

def main():
    toto(1, 2)


if __name__ == "__main__":
    main()