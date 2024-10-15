from abc import abstractmethod
from typing import List


class Observer:

    @abstractmethod
    def notify(self, observer,data):
        pass


class EventSource:
    def __init__(self):
        self._observers:List[Observer] = []

    def register(self, observer: Observer):
        self._observers.append(observer)

    def unregister(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self,data):
        for observer in self._observers:
            observer.notify(observer,data)


class LetterBoX(EventSource):
    def __init__(self):
        super().__init__()
        self.msg:[str] = []

    def  receive_message(self, msg):
        self.msg.append(msg)
        super().notify(msg)

class CyberAgent(Observer):
    def __init__(self):
        super().__init__()

    def notify(self, observer,data):
       print(f"Notifyed {data}")



if __name__ == '__main__':
    lb = LetterBoX()
    cb=CyberAgent()
    cb2 = CyberAgent()
    lb.register(cb)
    lb.register(cb2)
    lb.receive_message("test")

