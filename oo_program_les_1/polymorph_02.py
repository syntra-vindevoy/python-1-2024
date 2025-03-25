class IPrinter:
    def __init__(self):
        super().__init__()

    def print(self, s):
        raise NotImplementedError

class Printer(IPrinter):
    def __init__(self):
        super().__init__()


p: IPrinter = Printer()
print("hello world")