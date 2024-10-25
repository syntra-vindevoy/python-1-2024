# 1
# 11
# 21
# 1211
# 111221


def next_number(previous_number: int) -> int:
    previous_number = str(previous_number)
    len_previous = len(previous_number)
    result = ""
    for i in range(len_previous):
        if i == 0 or previous_number[i] != previous_number[i - 1]:
            count = 1
        else:
            count += 1

        if i == len_previous - 1 or previous_number[i] != previous_number[i + 1]:
            result += str(count) + previous_number[i]
    return int(result)


def print_sequence(n: int) -> None:
    result = 1
    print(result, end=" ")
    for i in range(n - 1):
        result = next_number(result)
        print(result, sep=" ", end=" ")


def get_sequence(n: int) -> list:
    result = 1
    result_list = [result]
    for i in range(n - 1):
        result = next_number(result)
        result_list.append(result)
    return result_list


def get_nth_item(n: int) -> str:
    result = "1"
    for i in range(n - 1):
        result = str(next_number(int(result)))
    return int(result)


def tests():
    assert next_number(1) == 11
    assert next_number(11) == 21
    assert next_number(21) == 1211
    assert next_number(1211) == 111221
    assert next_number(111221) == 312211
    assert get_nth_item(5) == 111221


def main():
    pass


if __name__ == "__main__":

    tests()
    print_sequence(5)
    print()
    print(get_nth_item(5))
    print(get_sequence(5))

    main()
