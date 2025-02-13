class Track:
    def __init__(self, x, y):
        self.__x = x  # Private attribute
        self.__y = y  # Private attribute

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


class Car(Track):
    def __init__(self, x, y, speed):
        super().__init__(x, y)
        self.__speed = speed  # Private attribute

    @property
    def speed(self):
        return self.__speed


# Example usage
car = Car(1, 2, 3)
print(car.x)  # Access private attribute via property
print(car.y)  # Access private attribute via property
print(car.speed)  # Access private attribute via property




car = Car(1,2,3)
print(car.x)
print(car.y)
print(car.speed)
