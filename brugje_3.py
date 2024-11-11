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
    return new_situation


def move_to_left(situation, person):
    new_situation = copy.deepcopy(situation)
    new_situation["right"].remove(person)
    new_situation["left"].append(person)
    new_situation["time_spent"] += person
    return new_situation


def get_combinations_move_to_right(situation):
    return combinations(situation["left"], 2)


def get_combinations_move_to_left(situation):
    return combinations(situation["right"], 1)


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
            new_situation = move_to_left(s, c[0])
            situations_new.append(new_situation)
    return situations_new


def main():
    situation_start = {"left": [1, 2, 5, 10], "right": [], "time_spent": 0}
    situations = [situation_start]
    situations = get_all_situations_moving_to_right(situations)
    print_all_situations(situations)
    situations = get_all_situations_moving_to_left(situations)
    print_all_situations(situations)


if __name__ == "__main__":
    main()
