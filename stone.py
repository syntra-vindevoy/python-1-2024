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


def get_solution(n):
    number_of_calculations = 0
    for l in [27, 0, -27]:
        for k in [9, 0, -9]:
            for j in [3, 0, -3]:
                for i in [1, 0, -1]:
                    total = l + k + j + i
                    number_of_calculations += 1
                    if total == n:
                        return l, k, j, i
    return None


def get_solution_version2(n):
    for l in [27, 0]:
        for k in [9, 0, -9]:
            for j in [3, 0, -3]:
                for i in [1, 0, -1]:
                    total = l + k + j + i
                    if total == n:
                        return l, k, j, i
    return None


def get_solution_version3(n):
    for l in [1, 0]:
        for k in [1, 0, -1]:
            for j in [1, 0, -1]:
                for i in [1, 0, -1]:
                    if 27 * l + 9 * k + 3 * j + i == n:
                        return l, k, j, i
    return None


def get_solution_version3(n):
    for l in [1, 0]:
        for k in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for i in [-1, 0, 1]:
                    if 27 * l + 9 * k + 3 * j + i == n:
                        return l, k, j, i
    return None


def get_solution_version4(n):
    for l in [27, 0]:
        for k in [-9, 0, 9]:
            for j in [-3, 0, 3]:
                for i in [-1, 0, 1]:
                    if l + k + j + i == n:
                        return l, k, j, i
    return None


def get_solution_version5(n):
    for l in [1, 0]:
        for k in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for i in [-1, 0, 1]:
                    if 27 * l + 9 * k + 3 * j + i == n:
                        return l, k, j, i
    return None


def get_solution_version6(n):

    stone_27 = 0
    stone_9 = 0
    stone_3 = 0
    stone_1 = 0

    if +27 - 9 - 3 - 1 <= n <= +27 + 9 + 3 + 1:
        stone_27 = +27
        n = n - 27
    else:
        stone_27 = 0

    if -9 - 3 - 1 <= n <= -9 + 3 + 1:
        stone_9 = -9
        n = n + 9
    elif +9 - 3 - 1 <= n <= +9 + 3 + 1:
        stone_9 = +9
        n = n - 9

    if -3 - 1 <= n <= -3 + 1:
        stone_3 = -3
        n = n + 3
    elif +3 - 1 <= n <= +3 + 1:
        stone_3 = +3
        n = n - 3

    if n == -1:
        stone_1 = -1
    elif n == +1:
        stone_1 = +1

    return stone_27, stone_9, stone_3, stone_1


def get_solution_version7(n):

    stone_27 = 0
    stone_9 = 0
    stone_3 = 0
    stone_1 = 0

    if +27 - 9 - 3 - 1 <= n <= +27 + 9 + 3 + 1:
        stone_27 = +27
        n = n - stone_27

    if -9 - 3 - 1 <= n <= -9 + 3 + 1:
        stone_9 = -9
    elif +9 - 3 - 1 <= n <= +9 + 3 + 1:
        stone_9 = +9
    n = n - stone_9

    if -3 - 1 <= n <= -3 + 1:
        stone_3 = -3
    elif +3 - 1 <= n <= +3 + 1:
        stone_3 = +3
    n = n - stone_3

    stone_1 = n

    return stone_27, stone_9, stone_3, stone_1


def get_solution_version8(n):

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

    """
    for i in range(1, 41):
        print(i, get_solution(i))
    for i in range(1, 41):
        print(i, get_solution_version2(i))
    """
    for i in range(1, 41):
        print(i, get_solution_version8(i))


if __name__ == "__main__":
    main()
