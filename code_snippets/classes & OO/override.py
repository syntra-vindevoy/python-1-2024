class Parent:
    def show(self):
        print("This is the parent class method")

class Child(Parent):
    def show(self):
        print("This is the child class method")

# Create an instance of Child
child_instance = Child()
child_instance.show()  # This will call the overridden method in the Child class