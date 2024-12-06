def btree_search(to_find: int, lower: int, higher: int, attempts: int = 1):
    middle = (lower + higher) // 2

    if middle == to_find:
        return attempts

    if to_find < middle:
        return btree_search(to_find, lower, middle - 1, attempts + 1)
    else:
        return btree_search(to_find, middle + 1, higher, attempts + 1)


def btree_search_while(to_find: int, lower: int, higher: int):
    attempts = 1

    while True:
        middle = (lower + higher) // 2

        if middle == to_find:
            return attempts

        if to_find < middle:
            higher = middle - 1
        else:
            lower = middle + 1

        attempts += 1


if __name__ == "__main__":
    higher = 10000

    print(max([btree_search_while(i + 1, 1, higher) for i in range(higher)]))
    print(sum([btree_search_while(i + 1, 1, higher) for i in range(higher)]))
