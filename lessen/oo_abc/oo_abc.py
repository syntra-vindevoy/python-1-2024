import abc


class AbcPrinter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def print(self, s):
        pass


class HPPrinter(AbcPrinter):
    def __init__(self):
        super().__init__()

    # def print(self, s):
    #    print("hp:", s)


class CanonPrinter(AbcPrinter):
    def __init__(self, s):
        super().__init__()

    def print(self, s):
        print("cannon:", s)
