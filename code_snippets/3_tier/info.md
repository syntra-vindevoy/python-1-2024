
info found on github-copilot and ajusted to 3 layers with initialiser

```python

# initializer
'''
from presentation import Presentation
from business_logic import BusinessLogic
from data_access import DataAccess
'''

def initialize():
    # Initialize data access layer
    data_access = DataAccess()
    # Initialize business logic layer with data access dependency
    business_logic = BusinessLogic(data_access)
    # Initialize presentation layer with business logic dependency
    presentation = Presentation(business_logic)
    return presentation

if __name__ == "__main__":
    presentation = initialize()
    presentation.run()


# presentation

class Presentation:
    def __init__(self, business_logic):
        self.business_logic = business_logic

    def run(self):
        user_input = input("Enter a value: ")
        result = self.business_logic.process_data(user_input)
        print(f"Processed result: {result}")


# logic

class BusinessLogic:
    def __init__(self, data_access):
        self.data_access = data_access

    def process_data(self, data):
        # Business logic processing
        processed_data = data.upper() # Example logic
        self.data_access.save_data(processed_data)
        return processed_data


# data

class DataAccess:
    def save_data(self, data):
    # Data storage logic
        with open("data.txt", "a") as file:
            file.write(data + "\n")
            print("Data saved successfully.")


```



