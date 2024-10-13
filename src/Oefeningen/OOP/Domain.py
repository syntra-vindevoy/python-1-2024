"""
Solid solution
"""
from typing import Iterable


class Product:
    def __init__(self, name, price, color, size):
        self._name = name
        self._price = price
        self._color = color
        self._size = size

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def color(self):
        return self._color

    @property
    def size(self):
        return self._size

    @name.setter
    def name(self, name):
        self._name = name

    @price.setter
    def price(self, price):
        self._price = price

    @color.setter
    def color(self, color):
        self._color = color

    @size.setter
    def size(self, size):
        self._size = size

    def __str__(self):
        return f"Product {self.name} {self.color} {self.size} {self.price}"

    def __repr__(self):
        return f"Product {self.name} {self.color} {self.size} {self.price}"


class SuperProduct(Product):
    def __init__(self, name, price, color, size, description):
        self.description = description
        super().__init__(name, price, color, size)

    def __str__(self):
        return f"Product {self.name} {self.color} {self.size} {self.price} {self.description}"

    def __repr__(self):
        return f"Product {self.name} {self.color} {self.size} {self.price} {self.description}"


class Store:
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


class Specification:
    def is_satisfied(self, product) -> bool:
        """
        Abstract methode
        Args:
            product:

        Returns:
            bool:
        """
        pass

    def __and__(self, other):
        """
        implement and
        Args:
            other:

        Returns:
            bool
        """
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        """
        Abstract methode to filter items
        Args:
            items:
            spec:
        """
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, product):
        """
        check if a product is satisfied by color
        Args:
            product:

        Returns:
            bool
        """
        return product.color == self.color


class TypeSpecification(Specification):
    def __init__(self, type_of):
        self.type_of = type_of

    def is_satisfied(self, product):
        """
        is type of
        Args:
            product:

        Returns:
            bool
        """
        return isinstance(product, self.type_of)


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, product) -> bool:
        """
        check if a product is satisfied by size
        Args:
            product:

        Returns:
            bool
        """
        return product.size == self.size


class AndSpecification(Specification):
    def __init__(self, spec1: Specification, spec2: Specification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, product) -> bool:
        """
        check if a product is satisfied by spec1 and spec2
        Args:
            product:

        Returns:
            bool
        """
        return self.spec1.is_satisfied(product) and self.spec2.is_satisfied(product)


class SpecificationFilter(Filter):

    def filter(self, items: Iterable, spec: Specification) -> Iterable:
        """
        Filter items
        Args:
            items:
            spec:

        Returns:
            object: 
        """
        for item in items:
            if spec.is_satisfied(item):
                yield item


class Color:
    BLUE = "Blue"
    GREEN = "Green"


class Size:
    LARGE = "Large"
    SMALL = "Small"
