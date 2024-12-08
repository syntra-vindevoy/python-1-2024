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
        name = input("Enter the name of the person: ")
        self.business_logic.add_person(str(name.strip()))

    def run(self):
        print()
        while self.running:

            menu_options = {
                '1': {
                    'description': "Print all persons", 
                    'action': self.print_all_persons
                    },
                '2': {
                    'description': "Add a person", 
                    'action': self.add_person
                    },
                'q': {
                    'description': "Quit", 
                    'action': lambda: setattr(self, 'running', False)
                    }
            }

            for key, value in menu_options.items():
                print(f"{key}. {value['description']}")
            print()
            choice = input("Enter your choice: ")
            print()

            action = menu_options.get(choice, {}).get('action', lambda: print("Invalid choice"))
            action()
            print()

        print(f"Exiting...\n")
        sleep(1)
            