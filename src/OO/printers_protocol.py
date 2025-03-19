from typing import Protocol


class Printer(Protocol):

    def print(self, s):
        ...

    def reset(self):
        ...


class HPPrinter:

    def print(self, s):
        print("hp:", s)

    def reset(self):
        print("resetting hp printer")


class CanonPrinter:

    def print(self, s):
        print("cannon:", s)

    def reset(self):
        print("resetting canon printer")


class Config:

    @staticmethod
    def get_printer() -> Printer:
        i = input("Which printer? 1 for HP, 2 for Canon: ")

        if i == "1":
            return HPPrinter()
        else:
            return CanonPrinter()


class Application:

    @staticmethod
    def output(new_printer: Printer):
        new_printer.print("hello world")


config = Config()
printer: Printer = config.get_printer()

app = Application()
app.output(printer)
