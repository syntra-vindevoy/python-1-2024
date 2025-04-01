
custs = [{}]

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address



class Customers:
    def __init__(self):
        self.customers = []

    def add(self, customer: Customer):
        self.customers.append(customer)

    def read(self):
        for cust in custs:
            c = Customer(cust["name"], cust["address"])
            self.add(c)


def main():
    c = Customer("John", "123 Main St")
    cs = Customers()
    cs.add(c)

    print(len(cs.customers))


if __name__ == "__main__":
    main()
