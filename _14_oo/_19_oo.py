#Polymorphism

class Printer:
    def __init__(self):
        super().__init__()

    def print(self, s):
        raise NotImplementedError("You forgot to implement the print method")


class HpPrinter(Printer):
    def __init__(self):
        super().__init__()

    def print(self, s):
        print("hp:", s)

class CanonPrinter(Printer):
    def __init__(self):
        super().__init__()

    def print(self, s):
        print("canon:", s)


hp = HpPrinter()
hp.print("Hello")

canon = CanonPrinter()
canon.print("Hello")

all_printers = [hp, canon]
for printer in all_printers:
    printer.print("Hello")