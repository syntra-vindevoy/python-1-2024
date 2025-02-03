def nested_sum(lists: list[int|float]) -> float:
    s = 0

    for lst in lists:
        for item in lst:
            s += item

    return s


def nested_sum2(lists: list[int|float]) -> float:
    return sum([sum(lst) for lst in lists])

if __name__ == '__main__':
    print(nested_sum2([[1, 2], [3, 4, 5], [6.0]]))
