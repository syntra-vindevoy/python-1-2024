import abc


class ABCPrinter(abc.ABC):
    @abc.abstractmethod
    def print(self, s):
        pass


class HPPrinter(ABCPrinter):
    def __init__(self):
        super().__init__()

    def print(self, s):
        print("hp:", s)


class Application:
    def __init__(self):
        super().__init__()

    def output(self, printer: ABCPrinter):
        printer.print("hello world")


printer = HPPrinter()

app = Application()
app.output(printer)
