from functools import wraps


def trace_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} - args: {args} - kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returns: {result}")
        return result

    return wrapper

