# 1, 3, 9, 27 = 40
# -1, -3, -9, -27 = -40


def get_solution_list():
    total_set = set()
    list = [1, 3, 9, 27]
    for i in [1, 0, -1]:
        for j in [3, 0, -3]:
            for k in [9, 0, -9]:
                for l in [27, 0, -27]:
                    total = i + j + k + l
                    if total > 0:
                        total_set.add(total)
    return total_set


def get_solution_version1(n):
    for l in [27, 0]:
        for k in [-9, 0, 9]:
            for j in [-3, 0, 3]:
                for i in [-1, 0, 1]:
                    if l + k + j + i == n:
                        return l, k, j, i
    return None


def get_solution_version2(n):

    stone_27 = 0
    stone_9 = 0
    stone_3 = 0
    stone_1 = 0

    # using stone 27
    if +27 - 9 - 3 - 1 <= n <= +27 + 9 + 3 + 1:
        stone_27 = +27
        n -= stone_27

    # using stone 9
    if +9 - 3 - 1 <= n <= +9 + 3 + 1:
        stone_9 = +9
    elif -9 - 3 - 1 <= n <= -9 + 3 + 1:
        stone_9 = -9

    n -= stone_9

    # using stone 3
    if -3 - 1 <= n <= -3 + 1:
        stone_3 = -3
    elif +3 - 1 <= n <= +3 + 1:
        stone_3 = +3

    n -= stone_3

    # using stone 1
    stone_1 = n

    return stone_27, stone_9, stone_3, stone_1


def main():
    print(get_solution_list())

    print()
    for i in range(1, 41):
        print(i, get_solution_version1(i))

    print()
    for i in range(1, 41):
        print(i, get_solution_version2(i))


if __name__ == "__main__":
    main()

# test
