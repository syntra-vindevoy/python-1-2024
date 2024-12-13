from datetime import datetime


def method_1(wrds: list[str]):
    lst = []

    for word in wrds:
        lst += [word]

    return lst


def method_2(wrds: list[str]):
    lst = []

    for word in wrds:
        lst.append(word.upper())

    return lst


def method_3(wrds: list[str]):
    return [word.upper() for word in sorted(wrds)]


def method_4(wrds: list[str]):
    lst = []

    for word in wrds:
        lst.extend([word])

    return lst


def main():
    times = 10000

    with open("../chapter9/words.txt", "r") as f:
        words = f.readlines()

    # start = datetime.now()
    # for _ in range(times):
    #     method_1(words)
    # end = datetime.now()
    # print(end - start)

    # start = datetime.now()
    # for _ in range(times):
    #     method_2(words)
    # end = datetime.now()
    # print(end - start)
    #

    start = datetime.now()
    for _ in range(times):
        method_3(words)
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    for _ in range(times):
        method_4(words)
    end = datetime.now()
    print(end - start)

    dc = {word: len(word) for word in words}


if __name__ == "__main__":
    main()
