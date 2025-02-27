from typing import List


class Contact:
    pass


class ContactList:
    def __init__(self):
        self.contacts = []


l = ContactList()

c = Contact()
l.contacts.append(c)


class Product:
    def __init__(self, name):
        self.name = name

class ProductList(list):
    def __init__(self):
        super().__init__()

    def append(self, product: Product):
        if type(product) != Product:
            raise TypeError("ProductList.append expects a Product")

        super().append(product)

l2 = ProductList()

p = Product("toto")

l2.append(p)

print(len(l2))

my_product: Product = l2[0]
my_product.name = "tata"

print(l2[0].name)

p1 = Product("titi")

l2.append(p1)
l2.append(c)

