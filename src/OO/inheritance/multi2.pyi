class Voertuig:
    def beweeg(self):
        print("Voertuig beweegt")


class Boot(Voertuig):
    def beweeg(self):
        print("Boot vaart")


class Auto(Voertuig):
    def beweeg(self):
        print("Auto rijdt")


class Amfibie(Auto, Boot):
    pass


a = Amfibie()
a.beweeg()
