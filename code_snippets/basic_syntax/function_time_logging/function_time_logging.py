import time
import logging
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Configure logging to save the log file in the script's directory
log_file_path = os.path.join(script_dir, 'execution_time.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO)

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

@time_it
def example_function():
    time.sleep(2)
    print("Function is running")

example_function()