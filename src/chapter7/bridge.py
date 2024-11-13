TIME_PERSONS = {
    "A": 1,
    "B": 2,
    "C": 5,
    "D": 10,}


def convert_to_dict(side):
    """
    Args:
        side: List of persons whose time data needs to be converted.

    Returns:
        A dictionary where each key is a person from the input list and the value is their corresponding time data from TIME_PERSONS.
    """
    my_dict = {}
    for person in side:
        my_dict[person] = (TIME_PERSONS[person])
    return my_dict.items()

def get_fastest(side:[],count)->[]:
    """
    Args:
        side: List of tuples where each tuple contains an item and a corresponding value
        count: Number of fastest items to return

    Returns:
        List of fastest items sorted by their corresponding value in ascending order
    """
    return [item[0] for item in sorted(convert_to_dict(side), key=lambda item: item[1])[:count]]


assert get_fastest(["A", "B", "C", "D"], 2) == ["A", "B"]


def get_slowest(side:[],count)->[]:
    """
    Args:
        side (list): A list of tuples where each tuple contains an item and its corresponding speed.
        count (int): The number of slowest items to retrieve.

    Returns:
        list: A list of items corresponding to the slowest speeds.
    """
    return [item[0] for item in sorted(convert_to_dict(side), reverse=True, key=lambda item: item[1])[:count]]


assert get_slowest(["A", "B", "C", "D"], 2) == ["D", "C"]


def move_too(pers_to_move: [], from_side: [], too_side: []) -> int:
    """
    :param pers_to_move: The list of persons to be moved.
    :param from_side: The list representing the side from which persons are moved.
    :param too_side: The list representing the side to which persons are moved.
    :return: The total time taken to move all persons.
    """
    total_time = 0
    for person in pers_to_move:
        from_side.remove(person)
        too_side.append(person)
        if total_time == 0 or total_time < TIME_PERSONS[person]:
            total_time = TIME_PERSONS[person]
    return total_time


def main():
    """
    Move A and B to the right side: Cost 2 seconds
    Move A back to the left side: Cost 1 second
    Move C and D to the right side: Cost 10 seconds
    Move B back to the left side: Cost 2 seconds
    Move A and B to the right side again: Cost 2 seconds
    Total time: 2 + 1 + 10 + 2 + 2 = 17 seconds"""
    right_side= []
    left_side = list(TIME_PERSONS.keys())
    total_time = 0

    while len(left_side) > 0:
        fastest = get_fastest(left_side, 2)
        total_time += move_too(fastest, left_side, right_side)
        print(left_side, right_side, total_time)

        fastest = get_fastest(right_side, 1)
        total_time += move_too(fastest, right_side, left_side)
        print(left_side, right_side, total_time)

        slowest = get_slowest(left_side, 2)
        total_time += move_too(slowest, left_side, right_side)
        print(left_side, right_side, total_time)

        fastest = get_fastest(right_side, 1)
        total_time += move_too(fastest, right_side, left_side)
        print(left_side, right_side, total_time)

        fastest = get_fastest(left_side, 2)
        total_time += move_too(fastest, left_side, right_side)
        print(left_side, right_side, total_time)


    print(total_time)

if __name__ == '__main__':
    main()