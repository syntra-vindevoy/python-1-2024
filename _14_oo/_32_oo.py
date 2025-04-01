class Person:
    # Constructor method to initialize the Person object with name and email
    def __init__(self, name: str, email: str):
        self.name = name  # Store the name of the person
        self.email = email  # Store the email address of the person

    # Static method to represent where the person lives (default is Earth)
    @staticmethod
    def lives_on_planet(where: str = "Earth"):
        return where  # Return the string representing the planet