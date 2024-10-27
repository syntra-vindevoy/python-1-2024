start_situation = [[1, 2, 5, 10], [], 0]


def move_to_right(num: int):
    if num in start_situation[0]:
        start_situation[0].remove(num)
        start_situation[1].append(num)
        return True
    return False


def move_right(
    person: int, start_situation: list[list[int], list[int], int]
) -> list[list[int], list[int], int]:
    new_situation = start_situation.copy()
    new_situation[0].remove(person)
    new_situation[1].append(person)
    return new_situation


def move_left(
    person: int, start_situation: list[list[int], list[int], int]
) -> list[list[int], list[int], int]:
    new_situation = start_situation.copy()
    new_situation[1].remove(person)
    new_situation[0].append(person)
    return new_situation


def main():
    print(start_situation)
    new_situation = start_situation.copy()
    new_situation = move_right(1, new_situation)
    print(new_situation)
    new_situation = move_left(1, new_situation)
    print(new_situation)
    """
    """


if __name__ == "__main__":
    main()
