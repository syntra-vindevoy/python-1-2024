from datetime import date  # Import the date class for handling dates


# Define a base class "Person" to represent a person's basic information and attributes
class Person:
    def __init__(self, name: str, email: str, dob: date = None):
        """
        Initialize a Person object with name, email, and optional date of birth (dob).
        :param name: The name of the person
        :param email: The email of the person
        :param dob: (Optional) Date of Birth of the person, default is None
        """
        self.name = name  # The person's name
        self.email = email  # The person's email address

        # Initialize private attributes (these attributes are typically meant for internal use)
        self._gender = None  # Placeholder for gender, not set here
        self.dob = None  # Placeholder for date of birth, not set here

    @property
    def age(self):
        """
        The `@property` decorator allows this `age` method to be accessed like an attribute,
        without requiring parentheses in the call (i.e., `person.age` rather than `person.age()`).

        For now, this simply returns a static value (52) as a placeholder for calculating the actual age.
        :return: Age (static value of 52)
        """
        x = 52  # Static age value for demonstration purposes
        return x


# Define a subclass "MalePerson" that inherits from the "Person" class
class MalePerson(Person):
    def __init__(self, name: str, email: str):
        """
        Initialize a MalePerson object, subclass of Person.
        :param name: The name of the person
        :param email: The email of the person
        """
        super().__init__(name, email)  # Call the parent class constructor
        self._gender = "Male"  # Set the gender to "Male" for this specific subclass


# Instantiate a MalePerson object named "yves"
yves = MalePerson("Yves", "<EMAIL>")
# Print the name of the person, along with their age
print(yves.name, "is", yves.age, "years old")