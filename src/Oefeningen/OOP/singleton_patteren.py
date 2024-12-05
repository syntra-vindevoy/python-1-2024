# classic implementation of Singleton Design pattern
class Singleton:
    """
    Summary of what the class does.

    This class implements the Singleton design pattern, ensuring that only one
    instance of the class can be created. It provides a global access point to
    that instance.

    :ivar __shared_instance: Holds the singleton instance.
    :type __shared_instance: Singleton or str
    """
    __shared_instance = 'Singleton'

    @staticmethod
    def get_instance():
        """Static Access Method"""
        if Singleton.__shared_instance == 'Singleton':
            Singleton()
        return Singleton.__shared_instance

    def __init__(self):
        """virtual private constructor"""
        if Singleton.__shared_instance != 'Singleton':
            raise Exception("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self


assert Singleton.get_instance() == Singleton.get_instance()

class Singleton2:
    _instance = None

    @classmethod
    def get_instance(cls, waarde=None):
        if cls._instance is None:
            cls._instance = cls(waarde)
        return cls._instance

    def __init__(self, waarde):
        if not hasattr(self, "waarde"):
            self.waarde = waarde



# main method
if __name__ == "__main__":

    # create object of Singleton Class
    try:
        obj = Singleton()
        print(obj)
    except Exception as e:
        print(e)

    # pick the instance of the class
    obj = Singleton.get_instance()
    print(obj)

    # Gebruik
    s1 = Singleton2.get_instance("Eerste")
    s2 = Singleton2.get_instance("Tweede")

    print(s1.waarde)  # Output: Eerste
    print(s2.waarde)  # Output: Eerste
    print(s1 is s2)  # Output: True
