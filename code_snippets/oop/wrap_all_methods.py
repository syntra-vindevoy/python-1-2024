import functools
import time

def log_execution_time(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Method {method.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper

def wrap_all_methods(cls):
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):
            setattr(cls, attr_name, log_execution_time(attr_value))
    return cls

@wrap_all_methods
class MyClass:
    def __init__(self, value):
        self.value = value

    def method_one(self):
        time.sleep(1)
        return self.value * 2

    def method_two(self):
        time.sleep(2)
        return self.value + 10

# Example usage
if __name__ == "__main__":
    obj = MyClass(5)
    print(obj.method_one())
    print(obj.method_two())