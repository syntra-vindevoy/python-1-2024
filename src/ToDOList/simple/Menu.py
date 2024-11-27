class Menu:
    def __init__(self, menu_data):
        self.menu_data = menu_data

    def show_menu(self):
        for key, value in self.menu_data.items():
            print(f"{key}: {value[0]}")

    @staticmethod
    def __get_user_choice():
        return input("Enter your choice: ")

    def start(self):
        while True:
            self.show_menu()
            choice = self.__get_user_choice()
            print(self.menu_data[str(choice)][0])
            if choice is not None and choice in self.menu_data:
                self.menu_data[str(choice)][1]()
