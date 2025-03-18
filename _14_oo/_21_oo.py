# Base interface for a printer class
class IPrinter:
    def __init__(self):
        super().__init__()

    # Abstract method that must be implemented by derived classes
    def print(self, s):
        raise NotImplemented


# Derived class for an HP printer implementing the IPrinter interface
class HpPrinter(IPrinter):
    def __init__(self):
        super().__init__()

    # Prints a string with "hp" as a prefix
    def print(self, s):
        print("hp:", s)


# Derived class for a Canon printer implementing the IPrinter interface
class CanonPrinter(IPrinter):
    def __init__(self):
        super().__init__()

    # Prints a string with "canon" as a prefix
    def print(self, s):
        print("canon:", s)


# Main application class which interacts with printers
class Application:
    def __init__(self):
        self.printer = None  # Placeholder for a printer instance

    # Method to prompt the user to choose a printer type (HP or Canon)
    def run(self):
        i = input("Which printer? 1 for HP, 2 for Canon:")

        # Instantiate the appropriate printer based on user input
        if i == "1":
            self.printer = HpPrinter()
        else:
            self.printer = CanonPrinter()

    # Outputs a message using the provided printer instance
    def output(self, printer: IPrinter):
        printer.print("Hello")


# Another application class with functionality similar to Application
class App2:
    def __init__(self):
        self.printer = None  # Placeholder for a printer instance

    # Method to prompt the user to choose a printer type (HP or Canon)
    def run(self):
        i = input("Which printer? 1 for HP, 2 for Canon:")

        # Instantiate the appropriate printer based on user input
        if i == "1":
            self.printer = HpPrinter()
        else:
            self.printer = CanonPrinter()

    # Outputs a message using the provided printer instance
    def output(self, printer: IPrinter):
        printer.print("Hello")


# Create an instance of the Application class
app = Application()

# Prompt the user to select a printer and assign it to the application's printer attribute
app.run()

# Access the selected printer
printer = app.printer

# Use the selected printer to output a message
app.output(printer)
