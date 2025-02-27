class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.ove = True

    def __str__(self):
        return f"{self.name} costs {self.price}"

    def calculate_total(self):
        return self.price * 10

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)



class Book(Item):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def calculate_total(self):

        return self.price * super().calculate_total()

    def __str__(self):
        return f"{self.name} by {self.author} costs {self.price}"


class BookStore(list):
    def __init__(self):
        super().__init__()

    def add_item(self, item: Item):
        self.append(item)

    def calculate_total(self):
        total = 0
        for itemer in self:
            total += itemer.calculate_total()
        return total

    class BookStore(set):
        def __init__(self):
            super().__init__()

        def add_item(self, item: Item):
            self.add(item)

        def calculate_total(self):
            total = 0
            for itemer in self:
                total += itemer.calculate_t

    def __str__(self):
        return f"Total: {self.calculate_total()}"


    def remove_item(self, item: Item):
        self.remove(item)



class BookkStoreClosed:
    def __init__(self):
        self.items: list[Book] = []


    def add_item(self, item: Book):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for itemer in self.items:
            total += itemer.calculate_total()
        return total


    def __str__(self):
        return f"Total: {self.calculate_total()}"

    def __iter__(self):
        return iter(self.items)



class Store:
    """
    class Store:

    def __init__(self):
        self.products = []

    def __iter__(self):
        """
    def __init__(self):
        self.products = []

    def  __iter__(self):
       """
        iterate over all products
       Returns:
            iterable: all products
       """
       self.index = 0  # Reset index for a new iteration
       return self

    def __next__(self):
        """
        get next product
        Returns:
            product: next product

        """
        if self.index < len(self.products):
            result = self.products[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration  # StopIteration is raised when there are no more items

    def add(self, product):
        """
        Add a product to the store
        Args:
            product:
        """
        self.products.append(product)

    def remove(self, product):
        """
        remove a product from the store
        Args:
            product:
        """
        self.products.remove(product)

    def all(self) -> list:
        """
        get all products in the store
        Returns:
            list

        """
        return self.products





b= Book("supernova", 5.5, "benoit")
c: Item =b
print(b)
b.name="nova"
b.ove="mike"
d = Book("supernova2", 5.5, "benoit")

print(b.calculate_total())
print(c.calculate_total())

book_store = BookkStoreClosed()
book_store.add_item(b)
book_store.add_item(c)
book_store.add_item(d)
print(book_store)

print(book_store.calculate_total())

for item in book_store:
    print(item.name)


book_store2 = BookStore()
book_store2.add_item(b)
book_store2.add_item(c)
book_store2.add_item(d)
print(book_store2)
names = [ x.name for x in book_store2]
print(names)

st= Store()
st.add(b)
st.add(c)
st.add(d)
for item in st:
    print(item.name)

names = [ x.name for x in st]
print(names)






