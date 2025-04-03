class TemperatureUtils:
    f_multi = 9 / 5
    f_add = 32

    @classmethod
    def convert_to_fahrenheit(cls, c):
        return c * cls.f_multi + cls.f_add


def main():
    print(TemperatureUtils.convert_to_fahrenheit(15))


if __name__ == "__main__":
    main()