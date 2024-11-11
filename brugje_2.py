from itertools import combinations
import copy
import pprint

START_SITUATION = {
    "left_people": [1, 2, 5, 10],
    "time_spent": 0,
    "right_people": [],
}


def get_new_situations_moving_to_right(situation):
    new_situations = []
    for combination in get_combinations_moving_to_right(situation):
        new_situation = move_to_right(situation, combination[0], combination[1])
        new_situations.append(new_situation)
    return new_situations


def get_new_situations_moving_to_left(situation):
    new_situations = []
    for person in get_combinations_moving_to_left(situation):
        new_situation = move_to_left(situation, person)
        new_situations.append(new_situation)
    return new_situations


def get_combinations_moving_to_right(situation):
    return list(combinations(situation["left_people"], 2))


def get_combinations_moving_to_left(situation):
    return list(combinations(situation["right_people"], 1))


def move_to_right(situation, person1, person2):
    new_situation = copy.deepcopy(situation)
    new_situation["left_people"].remove(person1)
    new_situation["left_people"].remove(person2)
    new_situation["right_people"].append(person1)
    new_situation["right_people"].append(person2)
    new_situation["time_spent"] += max(person1, person2)
    return new_situation


def move_to_left(situation, person):
    new_situation = copy.deepcopy(situation)
    new_situation["left_people"].append(person)
    new_situation["right_people"].remove(person)
    new_situation["time_spent"] += person
    return new_situation


def main():
    situations = [START_SITUATION]
    while situations:
        situation = situations.pop(0)
        new_situations = get_new_situations_moving_to_right(situation)
        new_situations.append(new_situations)
    situations = new_situations.copy()
    new_situations = []

    while situations:
        situation = situations.pop(0)
        new_situations = get_new_situations_moving_to_left(situation)
        new_situations.append(new_situations)
    situations = new_situations.copy()
    new_situations = []

    print(situations)


if __name__ == "__main__":
    main()
