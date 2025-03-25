class Printer:
    def __init__(self):
        super().__init__()

    def print(self, s):
        raise NotImplementedError("you forgot to implement the print method")


class HPPrinter(Printer):
    def __init__(self):
        super().__init__()

    def print(self, s):
        print("HPPrinter:", s)

class CanonPrinter(Printer):
    def __init__(self):
        super().__init__()

    def print(self, s):
        print("CannonPrinter:", s)

hp = HPPrinter()
canon = CanonPrinter()

all_printers = [hp, canon]

for printer in all_printers:
    printer.print("hello world")