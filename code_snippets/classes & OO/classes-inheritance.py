# Define the Animal class
class Animal:
    # Initialize the Animal object with name and species
    def __init__(self, name, species):
        self.name = name
        self.species = species

    @classmethod # Class method to set the kingdom attribute
    def set_kingdom(cls, kingdom):
        cls.kingdom = kingdom

    @staticmethod # Static method to check if an animal is a mammal
    def is_mammal(species):
        mammals = ["dog", "cat", "horse", "elephant", "human"]
        return species.lower() in mammals

    # Method to make the animal produce a sound
    def make_sound(self, sound):
        print(f"{self.name} the {self.species} says {sound}")

    # Method to print information about the animal
    def info(self):
        print(f"{self.name} is a {self.species}")

# Define the Dog class, which inherits from Animal
class Dog(Animal):
    # Initialize the Dog object with name and breed, and set species to "dog"
    def __init__(self, name, breed):
        super().__init__(name, "dog")  # Call the parent class's constructor
        self.breed = breed

    # Override the make_sound method to default to "woof"
    def make_sound(self, sound="woof"):
        super().make_sound(sound)  # Call the parent class's make_sound method

    # Override the info method to include breed information
    def info(self):
        super().info()  # Call the parent class's info method
        print(f"{self.name} is of breed {self.breed}")

# Create an instance of Animal
generic_animal = Animal("Generic", "animal")
generic_animal.make_sound("some sound")  # Output: Generic the animal says some sound
generic_animal.info()  # Output: Generic is a animal

print()

# Create an instance of Dog
buddy = Dog("Buddy", "Golden Retriever")
buddy.make_sound()  # Output: Buddy the dog says woof
buddy.info()  # Output: Buddy is a dog
              #         Buddy is of breed Golden Retriever

Animal.set_kingdom("Animalia")
print(Animal.kingdom)