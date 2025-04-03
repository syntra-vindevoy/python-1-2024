class Toto:
    def __init__(self):
        print("init")

    def __call__(self):
        print("Hello")


class Ticket:
    def __init__(self):
        print("init")
        self.count = 0

    def __call__(self):
        self.count += 1


t = Toto()

t()

tc = Ticket()

t1 = tc
print(t1())

print(t())

print(t1())

print(tc.count)
