class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add(self, *args, **kwargs):
        """
        Overloaded add method using *args and **kwargs.

        - If a single item is passed, adds it to storage.
        - If multiple items are passed as *args, adds them based on capacity.
        """
        if args:  # Check if arguments were passed via *args
            for item in args:
                if len(self.items) < self.capacity:
                    self.items.append(item)
                else:
                    print(f"Storage is full, can't add: {item}")
        elif kwargs.get("item_list"):  # Check if items are passed as 'item_list' in **kwargs
            item_list = kwargs["item_list"]
            for item in item_list:
                if len(self.items) < self.capacity:
                    self.items.append(item)
                else:
                    print(f"Storage is full, can't add: {item}")

    def __str__(self):
        return f"{self.items}"


if __name__ == "__main__":
    s = Storage(10)

    # Adding single items
    s.add("Apple")
    s.add("Banana")

    # Adding multiple items using *args
    s.add("Grapes", "Mango", "Orange", "Pineapple")
    print(s)

    # Adding multiple items as a list using **kwargs
    s.add(item_list=["Berry", "Papaya", "Peach", "Watermelon"])
    print(s)
