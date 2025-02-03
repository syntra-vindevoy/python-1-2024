from datetime import datetime


def solution_1():
    with open("words.txt") as file:
        words = file.readlines()

        lst = []

        for word in words:
            lst.append(word.strip())

        return lst


def solution_2():
    with open("words.txt") as file:
        words = file.readlines()

        lst = []

        for word in words:
            lst = lst + [word.strip()]

        return lst


if __name__ == "__main__":
    start = datetime.now()
    solution_1()
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    solution_2()
    end = datetime.now()
    print(end - start)
