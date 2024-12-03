from datetime import datetime


def method_1():
    print("method_1")


def method_2():
    print("method_2")


def method_3():
    print("method_3")


def method_4():
    print("method_4")


def method_5():
    print("method_5")


def method_6():
    print("method_6")


def method_7():
    print("method_7")


if __name__ == "__main__":

    functions = [
        method_1,
        method_2,
        method_3,
        method_4,
        method_5,
        method_6,
        method_7,
    ]
    for func in functions:
        func()

    print("---------------------------------------------------------")

    for i in range(1, 8):
        func = globals()[f"method_{i}"]  # globals returns all the global variables
        func()
