import time
from functools import wraps


def capture_time(func):
    @wraps(func)  # Preserve the original function's metadata
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Capture the start time
        print(f"Function '{func.__name__}' started at {start_time:.6f}")
        result = func(*args, **kwargs)  # Execute the actual function
        end_time = time.time()  # Capture the end time
        print(f"Function '{func.__name__}' ended at {end_time:.6f}")
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result  # Return the original function's result
    return wrapper


# Example usage
@capture_time
def example_function():
    print("Processing...")
    time.sleep(2)  # Simulate some processing time
    return "Result"


# Run the example function
print(example_function())
