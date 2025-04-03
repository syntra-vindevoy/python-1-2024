class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            print("Storage is full")

    def __str__(self):
        return f"{self.items}"


if __name__ == "__main__":
    s = Storage(10)
