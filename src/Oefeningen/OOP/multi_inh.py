class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal initialized: {self.name}")

    def speak(self):
        print(f"{self.name} makes some generic animal noise.")


class Dog(Animal):
    def __init__(self, name):
        print("Dog initialization start.")
        super().__init__(name)
        print("Dog initialization end.")

    def speak(self):
        print(f"{self.name} says woof.")


class Cat(Animal):
    def __init__(self, name):
        print("Cat initialization start.")
        super().__init__(name)
        print("Cat initialization end.")

    def speak(self):
        print(f"{self.name} says meow.")


class CatDog(Cat, Dog):
    def __init__(self, name):
        print("CatDog initialization start.")
        Cat.__init__(self,name)  # Cooperative initialization via MRO
        Dog.__init__(self,name)
        print("CatDog initialization end.")

    def speak(self):
        Dog.speak(self)  # Call Dog's speak directly
        Cat.speak(self)  # Call Cat's speak directly


# Example usage
cat_dog = CatDog("Fluffy")
print(cat_dog.name)
cat_dog.speak()
print(CatDog.__mro__)
