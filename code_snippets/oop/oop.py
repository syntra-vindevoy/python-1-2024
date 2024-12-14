class MyClass:
    # Class attribute
    class_attribute = "I am a class attribute"

    def __init__(self, value):
        # Instance attribute
        self.value = value

    # Instance method
    def basic_method(self):
        return f"The value is {self.value}"

    # Another instance method
    def increment_value(self, increment):
        self.value += increment
        return self.value

    # Class method
    @classmethod
    def get_class_attribute(cls):
        return cls.class_attribute

    # Static method
    @staticmethod
    def static_method():
        return "I am a static method"

    # Dunder method for string representation
    def __str__(self):
        return f"MyClass with value {self.value}"

    # Dunder method for official string representation
    def __repr__(self):
        return f"MyClass(value={self.value})"

    # Dunder method for addition
    def __add__(self, other):
        if isinstance(other, MyClass):
            return MyClass(self.value + other.value)
        return NotImplemented

    # Dunder method for equality
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.value == other.value
        return NotImplemented

    # Dunder method for length
    def __len__(self):
        return self.value

    # Dunder method for getting an item
    def __getitem__(self, key):
        return f"Item {key} from MyClass"

    # Dunder method for setting an item
    def __setitem__(self, key, value):
        print(f"Setting item {key} to {value} in MyClass")

    # Dunder method for deleting an item
    def __delitem__(self, key):
        print(f"Deleting item {key} from MyClass")

# Example usage
if __name__ == "__main__":
    # Creating an instance of MyClass
    obj = MyClass(10)
    
    # Calling instance methods
    print(obj.basic_method())  # Output: The value is 10
    print(obj.increment_value(5))  # Output: 15
    
    # Accessing class method
    print(MyClass.get_class_attribute())  # Output: I am a class attribute
    
    # Accessing static method
    print(MyClass.static_method())  # Output: I am a static method

    # Using dunder methods
    print(str(obj))  # Output: MyClass with value 15
    print(repr(obj))  # Output: MyClass(value=15)
    obj2 = MyClass(5)
    obj3 = obj + obj2  # Uses __add__
    print(obj3)  # Output: MyClass with value 20
    print(obj == obj2)  # Uses __eq__, Output: False
    print(len(obj))  # Uses __len__, Output: 15
    print(obj[1])  # Uses __getitem__, Output: Item 1 from MyClass
    obj[1] = "new value"  # Uses __setitem__
    del obj[1]  # Uses __delitem__