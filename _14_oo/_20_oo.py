# Interface-like class to define a contract for printing functionality
class IPrinter:
    def __init__(self):
        super().__init__()

    def print(self, s):
        # Abstract method – meant to be implemented by subclasses
        # Raises an exception if not overridden
        raise NotImplemented


# A concrete implementation of the IPrinter interface
class Printer(IPrinter):
    def __init__(self):
        super().__init__()


# Create an instance of Printer (subclass of IPrinter)
p: IPrinter = Printer()

# Attempt to invoke the 'print' method
# This will raise a 'NotImplementedError' because the 'print' method was not actually implemented in the Printer class
p.print("Hello")