class IPrinter:
    def __init__(self):
        super().__init__()

    def print(self, s):
        raise NotImplementedError("no print")


class Printer(IPrinter):
    def __init__(self):
        super().__init__()


p: IPrinter = Printer()
p.print("hello world")
