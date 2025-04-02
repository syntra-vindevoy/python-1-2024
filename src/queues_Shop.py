class Person:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Person({self.id}, {self.name})"

    def __repr__(self):
        return f"Person({self.id}, {self.name})"


class Shop:
    def __init__(self):
        self.queue = []
        self.current_index = 0

    def add_person(self, person: Person):
        self.queue.insert(0, person)

    def get_next_person(self):
        if len(self.queue) > 0:
            # Retrieve and remove the last person from the queue
            return self.queue.pop(len(self.queue) - 1)
        else:
            return None  # Handle edge case if queue is empty

    def __iter__(self):
        # Reset the index for a fresh iteration every time `iter()` is called
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.queue):
            raise StopIteration
        person = self.queue[self.current_index]
        self.current_index += 1
        return person

    def __str__(self):
        return str(self.queue)


def main():
    shop = Shop()
    shop.add_person(Person(1, "Peter"))
    shop.add_person(Person(2, "Anna"))
    shop.add_person(Person(3, "Maria"))
    shop.add_person(Person(4, "John"))
    shop.add_person(Person(5, "Jane"))
    shop.add_person(Person(6, "Jack"))
    shop.add_person(Person(7, "Jill"))

    print(shop)

    print(shop.get_next_person())
    print(shop.get_next_person())
    print(shop.get_next_person())
    print(shop.get_next_person())
    print("------------------------")
    for person in shop:
        print(person)
    print("------------------------")
    print(shop.get_next_person())
    print("------------------------")
    for person in shop:
        print(person)


if __name__ == "__main__":
    main()
