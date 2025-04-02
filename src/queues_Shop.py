class Person:
    def __init__(self, id, name, age):
        self.name = name
        self.id = id
        self.age = age

    def __str__(self):
        return f"Person({self.id}, {self.name}, {self.age})"

    def __repr__(self):
        return f"Person({self.id}, {self.name}), {self.age})"


class Shop:
    def __init__(self):
        self.queue = []
        self.current_index = 0

    def add_person(self, person: Person):
        """
        Adds a Person object to the queue. If the person is aged 50 or older, they are appended
        to the end of the queue. Otherwise, they are added at the beginning of the queue.

        :param person: A `Person` object to be added to the queue.
        :type person: Person
        :return: None
        """

        if person.age >= 50:
            self.queue.append(person)
        else:
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
    shop.add_person(Person(1, "Peter", 30))
    shop.add_person(Person(2, "Anna", 30))
    shop.add_person(Person(3, "Maria", 50))
    shop.add_person(Person(4, "John", 50))
    shop.add_person(Person(5, "Jane", 10))
    shop.add_person(Person(6, "Jack", 50))
    shop.add_person(Person(7, "Jill", 10))
    print("------------------------")
    for person in shop:
        print(person)
    print("------------------------")
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
