class TempUtils:

    @classmethod
    def add(cls, a, b):
        return a + b

    f_multi = 9/5
    f_add = 32

    @classmethod
    def convert_celsius_to_fahrenheit(cls, c):
        return c * cls.f_multi + cls.f_add



def main():
    print(TempUtils.add(1, 2))
    print(TempUtils.convert_celsius_to_fahrenheit(15))


if __name__ == "__main__":
    main()