"""
Solid solution
"""
class Product:
    def __init__ (self, name, price, color, size):
        self.name = name
        self.price = price
        self.color = color
        self.size = size

    def __str__ (self):
        return f"Product {self.name} {self.color} {self.size} {self.price}"

    def __repr__ (self):
        return f"Product {self.name} {self.color} {self.size} {self.price}"

class Store:
    def __init__ (self):
        self.products = []

    def add (self, product):
        """
        Add a product to the store
        Args:
            product:
        """
        self.products.append (product)

    def remove (self, product):
        """
        remove a product from the store
        Args:
            product:
        """
        self.products.remove (product)

    def all (self) -> list:
        """
        get all products in the store
        Returns: 
            list

        """
        return self.products


class Specification:
    def is_satisfied (self, product)->bool:
        """
        Abstract methode
        Args:
            product:

        Returns:
            bool:
        """
        pass

    def __and__(self, other)->bool:
        """
        implement and
        Args:
            other:

        Returns:
            bool
        """
        return AndSpecification (self, other)


class Filter:
    def filter (self, items, spec):
        """
        Abstract methode to filter items
        Args:
            items:
            spec:
        """
        pass


class ColorSpecification (Specification):
    def __init__ (self, color):
        self.color = color

    def is_satisfied (self, product):
        """
        check if a product is satisfied by color
        Args:
            product:

        Returns:
            bool
        """
        return product.color == self.color


class SizeSpecification (Specification):
    def __init__ (self, size):
        self.size = size

    def is_satisfied (self, product)->bool:
        """
        check if a product is satisfied by size
        Args:
            product:

        Returns:
            bool
        """
        return product.size == self.size


class AndSpecification (Specification):
    def __init__ (self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied (self, product)->bool:
        """
        check if a product is satisfied by spec1 and spec2
        Args:
            product:

        Returns:
            bool
        """
        return self.spec1.is_satisfied (product) and self.spec2.is_satisfied (product)


class BetterFilter (Filter):

    def filter (self, items, spec):
        """
        Filter items
        Args:
            items:
            spec:
        """
        for item in items:
            if spec.is_satisfied (item):
                yield item


class Color:
    BLUE = "Blue"
    GREEN = "Green"


class Size:
    LARGE = "Large"
    SMALL = "Small"


