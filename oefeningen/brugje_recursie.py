import copy
from itertools import combinations
from pprint import pprint


def move_to_right(situation, person1, person2):
    new_situation = copy.deepcopy(situation)
    new_situation["left"].remove(person1)
    new_situation["left"].remove(person2)
    new_situation["right"].append(person1)
    new_situation["right"].append(person2)
    new_situation["time_spent"] += max(person1, person2)
    new_situation[
        "description"
    ] += f"Move {person1} and {person2} to right, added: {max(person1, person2)}\n"
    return new_situation


def move_to_left(situation, person):
    new_situation = copy.deepcopy(situation)
    new_situation["right"].remove(person)
    new_situation["left"].append(person)
    new_situation["time_spent"] += person
    new_situation["description"] += f"Move {person} to left, added:{person} \n"
    return new_situation


def get_combinations_move_to_right(situation):
    return combinations(situation["left"], 2)


def get_combinations_move_to_left(situation):
    return situation["right"]


def print_all_situations(situations):
    print()
    for s in situations:
        pprint(s)


def get_all_situations_moving_to_right(situations):
    situations_new = []
    for s in situations:
        for c in get_combinations_move_to_right(s):
            new_situation = move_to_right(s, c[0], c[1])
            situations_new.append(new_situation)
    return situations_new


def get_all_situations_moving_to_left(situations):
    situations_new = []
    for s in situations:
        for c in get_combinations_move_to_left(s):
            new_situation = move_to_left(s, c)
            situations_new.append(new_situation)
    return situations_new


def filter_fastest_solutions(situations):
    fastest_time = min([s["time_spent"] for s in situations])
    return [s for s in situations if s["time_spent"] == fastest_time]


def main():
    situation_start = {
        "left": [1, 2, 5, 10],
        "right": [],
        "time_spent": 0,
        "description": "",
    }
    situations = [situation_start]

    situations = get_all_situations_moving_to_right(situations)
    situations = get_all_situations_moving_to_left(situations)

    situations = get_all_situations_moving_to_right(situations)
    situations = get_all_situations_moving_to_left(situations)

    situations = get_all_situations_moving_to_right(situations)
    # print_all_situations(situations)

    print()
    print("these are the fastest solutions:")
    print_all_situations(filter_fastest_solutions(situations))


if __name__ == "__main__":
    main()
