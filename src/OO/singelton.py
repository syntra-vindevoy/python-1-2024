class Singleton(type):
    _instances = {}

    def __new__(cls, name, bases, class_dict):
        # Properly define the __new__ method to accept required arguments
        return super().__new__(cls, name, bases, class_dict)

    def __call__(cls, *args, **kwargs):
        # Implement the singleton behavior
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
