custs = [
    {"name": "John", "address": "123 Main St"},
    {"name": "Jane", "address": "456 Main St"},
]

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Customers:
    def __init__(self):
        self.customers = []

    def add(self, customer: Customer):
        self.customers.append(customer)

    @classmethod
    def read(cls):
        customers = Customers()

        for cust in custs:
            c = Customer(cust["name"], cust["address"])
            customers.add(c)

        return customers


def main():
    cs = Customers.read()

    print(len(cs.customers))

if __name__ == "__main__":
    main()
