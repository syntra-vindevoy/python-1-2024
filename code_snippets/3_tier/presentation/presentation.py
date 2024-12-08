from time import sleep

class Presentation:
    def __init__(self, business_logic):
        self.business_logic = business_logic

    def print_all_persons(self):
        persons = self.business_logic.get_all_persons()
        for person in persons:
            print(person.get_person_details())

    def add_person(self, name:str):
        self.business_logic.add_person(name)

    def run(self):
        running = True
        while running:
            print("1. Print all persons")
            print("2. Add a person")
            choice = input("Enter your choice: ")

            if choice == '1': self.print_all_persons()
            elif choice == '2':
                name = input("Enter the name of the person: ")
                self.add_person(name)
            elif choice == 'q':
                running = False
            else:
                print("Invalid choice")
        print("Exiting...")
        sleep(2)
            