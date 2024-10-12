from Oefeningen.OOP.Domain import Product, Color, Size, BetterFilter, Store, ColorSpecification, SizeSpecification, \
    AndSpecification

if __name__ == '__main__':
    apple = Product ("apple", 99.99, Color.GREEN, Size.SMALL)
    tree = Product ("tree", 4.99, Color.GREEN, Size.LARGE)
    house = Product ("house", 44.7, Color.BLUE, Size.LARGE)

    store_products = Store ()
    store_products.add (apple)
    store_products.add (tree)
    store_products.add (house)

    print("All products")
    print("------------")
    print (store_products.all ())
    print("\n")
    print ("All products GREEN")
    print ("------------")
    bf = BetterFilter ()
    green = ColorSpecification (Color.GREEN)
    for product in bf.filter (store_products.products, green):
        print (product)
    print ("\n")
    print ("All products LARGE")
    print ("------------")
    large = SizeSpecification (Size.LARGE)
    for product in bf.filter (store_products.products, large):
        print (product)
    print ("\n")
    print ("All products large and green")
    print ("------------")
    for product in bf.filter (store_products.products, AndSpecification (large, green)):
        print (product)
    print ("\n")
    print ("All products large and green")
    print ("------------")
    for product in bf.filter (store_products.products, large & ColorSpecification (Color.GREEN)):
        print (product)
