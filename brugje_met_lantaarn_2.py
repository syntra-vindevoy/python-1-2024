situation_left = [1, 2, 5, 10]
situation_right = []

situation = [situation_left, situation_right, 0]
situations = [situation]


def move_right(
    personA: int,
    personB: int,
    start_situation: list[list[int], list[int], int],
) -> tuple[list[int], list[int], int]:

    new_situation_left = start_situation[0].copy()
    new_situation_left.remove(personA)
    new_situation_left.remove(personB)

    new_situation_right = start_situation[1].copy()
    new_situation_right.append(personA)
    new_situation_right.append(personB)

    new_time_spent = start_situation[2]
    new_time_spent += max(personA, personB)

    return [new_situation_left, new_situation_right, new_time_spent]


def move_left(
    person: int,
    start_situation: list[list[int], list[int], int],
) -> tuple[list[int], list[int], int]:

    new_situation_left = start_situation[0].copy()
    new_situation_left.append(person)

    new_situation_right = start_situation[1].copy()
    new_situation_right.remove(person)

    new_time_spent = start_situation[2]
    new_time_spent += person

    return [new_situation_left, new_situation_right, new_time_spent]


def main():
    situation_left = [1, 2, 5, 10]
    situation_right = []

    situation = [situation_left, situation_right, 0]
    situations = [situation]

    while True:
        for situation in situations:
            generate_new_situations_moving_to_right(situation, situations)


def tests():
    assert move_right(1, 2, [[1, 2, 5, 10], [], 0]) == [[5, 10], [1, 2], 2]
    assert move_left(1, [[5, 10], [1, 2], 2]) == [[5, 10, 1], [2], 3]
    pass


if __name__ == "__main__":
    main()
