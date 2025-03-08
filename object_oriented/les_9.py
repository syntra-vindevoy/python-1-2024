class Contact:
    pass

# class Contactlist:
#     def __init__(self):
#         self.contacts = []
# c = Contact()
# l = Contactlist()
# l.contacts.append(c)

class Product:
    def __init__(self, name):
        self.name = name

class Productlist(list):
    pass

l2 = Productlist()
p = Product("titi")

l2.append(p)
# print (len(l2))
#
# print(l2[0].name)

"""volgende versie"""

class Product:
    def __init__(self, name):
        self.name = name

class Productlist(list):
    def __init__(self):
        super().__init__()
    def append(self, product: Product):
        if type(product) != Product:
            raise TypeError("Argument must be of type Product.")
        super().append(product)

l2 = Productlist()
p = Product("titi")

l2.append(p)

print (len(l2))