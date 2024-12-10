from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Fisch(Animal):
    def blub(self):
        return "Blub!"

# Example usage
if __name__ == "__main__":

    dog = Dog()
    print(dog.make_sound(),"",sep="\n")  # Output: Woof!

    cat = Cat()
    print(cat.make_sound(),"",sep="\n")  # Output: Woof!
    
    fish = Fisch()  # This will raise an error because Fisch does not implement make_sound    
