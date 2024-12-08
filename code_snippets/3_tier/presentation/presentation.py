from time import sleep

class Presentation:
    def __init__(self, business_logic):
        self.business_logic = business_logic
        self.running = True

    def print_all_persons(self):
        persons = self.business_logic.get_all_persons()
        for person in persons:
            print(person.get_person_details())

    def add_person(self):
        self.business_logic.add_person(input("Enter the name of the person: "))

    def run(self):
        while self.running:

            print("1. Print all persons")
            print("2. Add a person")
            print('q, Quit')

            choice = input("Enter your choice: ")

            actions = {
                '1': self.print_all_persons,
                '2': self.add_person,
                'q': lambda: setattr(self, 'running', False)
            }

            action = actions.get(choice, lambda: print("Invalid choice"))
            action()

        print("Exiting...")
        sleep(2)
            