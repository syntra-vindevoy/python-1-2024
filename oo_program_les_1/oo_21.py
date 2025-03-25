class IPrinter:
    def __init__(self):
        super().__init__()

    def print(self, s):
        raise NotImplementedError("no print")


class HPPrinter(IPrinter):
    def __init__(self):
        super().__init__()

    def print(self, s):
        print("hp:", s)


class CanonPrinter(IPrinter):
    def __init__(self):
        super().__init__()

    def print(self, s):
        print("cannon:", s)


class Config:
    def __init__(self):
        super().__init__()

    def get_printer(self) -> IPrinter:
        i = input("Which printer? 1 for HP, 2 for Canon: ")

        if i == "1":
            return HPPrinter()
        else:
            return CanonPrinter()


class Application:
    def __init__(self):
        super().__init__()

    def output(self, printer: IPrinter):
        printer.print("hello world")


config = Config()
printer = config.get_printer()

app = Application()
app.output(printer)
