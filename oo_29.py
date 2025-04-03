import time


def retries(num_retries, sleep_time=60):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print(f"Attempt {attempt} failed with error: {e}")
                    if attempt >= num_retries:
                        print("Reached maximum retries. Raising the last exception.")
                        raise

                time.sleep(sleep_time)
        return wrapper

    return decorator


# Example usage
@retries(num_retries=5, sleep_time=300)
def might_fail():
    # Example function that raises an exception
    print("Trying something risky...")
    raise ValueError("An intentional error occurred!")


# Calling the function will cause retries
try:
    might_fail()
except Exception as e:
    print(f"Final exception caught after retries: {e}")