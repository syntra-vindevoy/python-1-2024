from abc import ABC, abstractmethod


class AbstractPrinter(ABC):

    @abstractmethod
    def print(self, s):
        pass


class HPPrinter(AbstractPrinter):

    def print(self, s):
        print("hp:", s)


class CanonPrinter(AbstractPrinter):

    def print(self, s):
        print("cannon:", s)


class Config:

    @staticmethod
    def get_printer() -> AbstractPrinter:
        i = input("Which printer? 1 for HP, 2 for Canon: ")

        if i == "1":
            return HPPrinter()
        else:
            return CanonPrinter()


class Application:


    @staticmethod
    def output(new_printer: AbstractPrinter):
        new_printer.print("hello world")


config = Config()
printer = config.get_printer()

app = Application()
app.output(printer)
