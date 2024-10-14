from src.Oefeningen.OOP.Domain import SpecificationFilter, Product, Color, Size, SuperProduct, Store, \
    ColorSpecification, SizeSpecification, AndSpecification
import unittest

class SpecificationFilterTest(unittest.TestCase):
    def test_filter(self):
        apple = Product("apple22", 99.99, Color.GREEN, Size.SMALL)
        tree = Product("tree22", 4.99, Color.GREEN, Size.LARGE)
        house = Product("house22", 44.7, Color.BLUE, Size.LARGE)
        super_house = SuperProduct("house22", 44.7, Color.BLUE, Size.LARGE, "Test vam superhouse")

        store_products = Store()
        store_products.add(apple)
        store_products.add(tree)
        store_products.add(house)
        store_products.add(super_house)
        sp = SpecificationFilter()

        green = ColorSpecification(Color.GREEN)
        result=[]
        for product in sp.filter(store_products, green):
            result.append(product)
        self.assertEqual(len(result),2,'Must be 2')


    def test_filter_and_specification(self):
        apple = Product("apple2sd2", 99.99, Color.GREEN, Size.SMALL)
        tree = Product("tree2sds2", 4.99, Color.GREEN, Size.LARGE)
        house = Product("housesd22", 44.7, Color.BLUE, Size.LARGE)
        super_house = SuperProduct("housesd22", 44.7, Color.BLUE, Size.LARGE, "Test vam superhouse")
        store_products = Store()
        store_products.add(apple)
        store_products.add(tree)
        store_products.add(house)
        store_products.add(super_house)
        sp = SpecificationFilter()
        green = ColorSpecification(Color.GREEN)
        large = SizeSpecification(Size.LARGE)
        result = []
        for product in sp.filter(store_products, AndSpecification(large, green)):
            result.append(product)
        self.assertEqual(len(result), 1, 'Must be 1')

