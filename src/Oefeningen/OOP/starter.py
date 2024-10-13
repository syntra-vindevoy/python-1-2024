from src.Oefeningen.OOP.Domain import Product, Color, Size, Store, ColorSpecification, \
    SizeSpecification, \
    AndSpecification, TypeSpecification, SpecificationFilter

from src.Oefeningen.OOP.Domain import SuperProduct

if __name__ == '__main__':
    apple = Product ("apple", 99.99, Color.GREEN, Size.SMALL)
    tree = Product ("tree", 4.99, Color.GREEN, Size.LARGE)
    house = Product ("house", 44.7, Color.BLUE, Size.LARGE)
    super_house = SuperProduct("house", 44.7, Color.BLUE, Size.LARGE,"Test vam superhouse")

    store_products = Store ()
    store_products.add (apple)
    store_products.add (tree)
    store_products.add (house)
    store_products.add(super_house)

    print("All products")
    print("------------")
    print (store_products.all ())
    print("\n")
    print ("All products GREEN")
    print ("------------")
    bf = SpecificationFilter ()
    green = ColorSpecification (Color.GREEN)
    for product in bf.filter (store_products, green):
        print (product)
    print ("\n")
    print ("All products LARGE")
    print ("------------")
    large = SizeSpecification (Size.LARGE)
    for product in bf.filter (store_products, large):
        print (product)
    print ("\n")
    print ("All products large and green")
    print ("------------")
    for product in bf.filter (store_products, AndSpecification (large, green)):
        print (product)
    print ("\n")
    print ("All products large and green")
    print ("------------")
    for product in bf.filter (store_products, large & ColorSpecification (Color.GREEN)):
        print (product)
    print("\n")
    print("All products type super")
    print("------------")
    type_of = TypeSpecification (type(super_house))
    for product in bf.filter(store_products, type_of):
        print(product)