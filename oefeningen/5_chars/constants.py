import string

class Constant:
    def __init__(self, value):
        self._value = value  # Directly assign to the private attribute
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        raise AttributeError("Cannot change value of a constant")
    
    def __str__(self):
        return str(self._value)
    
    def __repr__(self):
        return f"Constant({self._value!r})"
    
    def __add__(self, other):
        if isinstance(other, str):
            return str(self._value) + other
        return NotImplemented

ALPHABET = Constant(string.ascii_lowercase)




