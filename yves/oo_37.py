class TicketCounter:
    def __init__(self):
        super().__init__()

        self.count = 0

    def __call__(self):
        self.count += 1

        return self.count

tc = TicketCounter()

ticket = tc()

print(ticket)

ticket = tc()
print(ticket)

