import queue
import threading
import time
import uuid

"""
First try at a concurrent system
author : Benoit Goethals
"""


class Storage:
    """
    Class for managing a thread-safe queue with monitoring capabilities.

    The Storage class provides a way to store and retrieve data
    using a locking mechanism to ensure thread safety. It includes
    a method to continuously monitor and print the size of the
    queue at regular intervals. This class is ideal for concurrent
    applications where multiple threads need to access a shared
    resource.

    :ivar __string_qeuue: A private queue used to store string data.
    :type __string_qeuue: queue.Queue
    :ivar lock: A lock object to ensure thread-safe operations on
                the queue.
    :type lock: threading.Lock
    """

    def __init__(self):
        self.__string_qeuue = queue.Queue()
        self.lock = threading.Lock()

    def put(self, data):
        with self.lock:
            self.__string_qeuue.put(data)

    def get(self) -> str:
        with self.lock:
            return self.__string_qeuue.get()

    def monitor(self):
        while True:
            time.sleep(1)
            print(f"size: {self.__string_qeuue.qsize()}")

    def starter(self):
        thread = threading.Thread(target=self.monitor)
        thread.start()


class Consumer:
    """
    Consumer class responsible for managing data retrieval from storage using
    a separate thread. It continuously fetches data in regular intervals and
    prints the retrieved information.

    The class is initialized with a storage object and utilizes a threading
    mechanism to obtain data without blocking the main execution flow.

    :ivar storage: The storage object from which data is retrieved.
    :type storage: Storage
    :ivar lock: A threading lock to ensure thread-safe access.
    :type lock: threading.Lock
    """

    def __init__(self, storage: Storage):
        self.storage = storage
        self.lock = threading.Lock()

    def __get(self) -> str:
        return storage.get()

    def starter(self):
        def getter():
            while True:
                time.sleep(2)
                r = self.__get()
                print(f"Got {r}")

        thread = threading.Thread(target=getter)
        thread.start()


class Producer:
    """
    This class represents a Producer that generates unique data and puts it
    into a storage system continuously. It manages access to shared resources
    using threading and ensures synchronization.

    The Producer is designed to run its operations in a separate thread to
    allow uninterrupted data generation and storage. It uses a lock to
    synchronize access to the storage, ensuring thread safety when interacting
    with shared resources.

    :ivar storage: The storage system where the data produced by this producer
                   is stored. The storage must implement a `put` method to
                   accept data.
    :type storage: Storage
    :ivar lock: A threading lock to ensure that only one thread accesses the
                storage system at any time.
    :type lock: threading.Lock
    """

    def __init__(self, storage: Storage):
        self.storage = storage
        self.lock = threading.Lock()

    def starter(self):
        def putter():
            while True:
                self.__put(str(uuid.uuid4()))
                time.sleep(1)

        thread = threading.Thread(target=putter)
        thread.start()

    def __put(self, data):
        storage.put(data)
        print(f"Put {data}")


if __name__ == '__main__':
    storage = Storage()
    consumers = []
    producers = []
    for i in range(10):
        consumers.append(Consumer(storage))
        producers.append(Producer(storage))

    storage.starter()
    for producer in producers:
        producer.starter()
    for consumer in consumers:
        consumer.starter()

    while True:
        pass
