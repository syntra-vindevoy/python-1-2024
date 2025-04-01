"""Exception handling example."""
import math
from doctest import UnexpectedException

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)
class Polygon:
    def __init__(self):
     self.vertices = []
    def add_point(self, point):
      self.vertices.append((point))
    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter

class Connection:
    def save(self, customer):
        print(f"Saving customer {customer}")

    def close(self):
        pass

    def __init__(self, points=None):
        points = points if points else []

        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
        self.vertices.append(point)


class InvalidNumberError(Exception):

    def __init__(self, message="Invalid number provided"):
        self.message = message
        super().__init__(self.message)


def guess_number(x:int)->int:
   if type(x) != int:
       raise TypeError("x must be an integer")
   if not x > 0:
       raise InvalidNumberError("x must be greater than 0")  # Raise custom exception here

   return x


def get_connections():
    return Connection()


class Customer:
   def __init__(self, name, age, email):
       self.name = name
       self.age = age
       self.email = email





def save_customer(customer:Customer):
    db=None
    try:
        db = get_connections()
        db.save(customer)
    except Exception as e:
         if db is not None or db ==[]:
             db.close()


def handle_user_guess(user_input: str) -> int:
    try:
        number = int(user_input)
        return guess_number(number)
    except (InvalidNumberError, TypeError, ValueError) as e:
       raise e

def foo(x:int):

      return 5/x






if __name__ == "__main__":
    try:
        user_input = input("Enter a number: ")
        inp = handle_user_guess(user_input)
        print(foo(inp))
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
