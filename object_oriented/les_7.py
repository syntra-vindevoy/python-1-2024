class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
my_car = Car('Ford', 'Custom', 2020)
son_car = Car("Volkswagen", "Fox", 2005)

print (my_car.make)
print (son_car.make)

Car.color = "Blue"
my_car.color = "Grey"
print (my_car.color)
print (son_car.color)



