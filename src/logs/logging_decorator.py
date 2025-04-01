import time
from functools import wraps

from src.logs.log_manager import LogManager
from src.logs.type_logger_enum import TypeLogger


def trace_func(func):
    @wraps(func)  # Preserve the original function's metadata
    def wrapper(*args, **kwargs):
        logger = LogManager.get_logger(type_logger=TypeLogger.Console, name=func.__name__)
        start_time = time.time()  # Capture the start time
        logger.info(f"Function '{func.__name__}' started at {start_time:.6f}")

        result = func(*args, **kwargs)  # Execute the actual function

        end_time = time.time()  # Capture the end time
        logger.info(f"Function '{func.__name__}' ended at {end_time:.6f}")
        logger.info(f"Execution time: {end_time - start_time:.6f} seconds")

        return result  # Return the original function's result

    return wrapper
