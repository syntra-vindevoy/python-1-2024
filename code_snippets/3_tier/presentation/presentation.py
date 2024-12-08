# presentation

class Presentation:
    def __init__(self, business_logic):
        self.business_logic = business_logic

    def process_data(self,value):
        result = self.business_logic.process_data(value)
        print(f"Processed result: {result}")

    def get_storage_content(self):
        return self.business_logic.get_data()

    def print_storage_content(self):
        print(f"content:{self.get_storage_content()}")

    def run(self):
        running = True
        while running:
            user_input = input("Enter a value: ")
            self.process_data(user_input)
            self.print_storage_content()


