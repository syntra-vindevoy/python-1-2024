import random


def btree_search(to_find: int, lower: int, higher: int, attempts: int = 1):
    middle = (lower + higher) // 2

    if middle == to_find:
        print("found it:", middle)
        return attempts

    if to_find < middle:
        return btree_search(to_find, lower, middle, attempts + 1)
    else:
        return btree_search(to_find, middle + 1, higher, attempts + 1)


if __name__ == "__main__":
    higher = 10000

    print(max([btree_search(i + 1, 1, higher) for i in range(10000)]))

