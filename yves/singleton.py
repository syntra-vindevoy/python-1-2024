class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Highlander(metaclass=Singleton):
    def __init__(self, name):
        print("enter init")
        print(name)
        self.name = name
        print("exit init")

    def die(self):
        print("There goes", self.name, "'s head")

def main():
    sean = Highlander("sean")
    chris = Highlander("chris")

    sean.die()
    chris.die()

if __name__ == "__main__":
    main()
