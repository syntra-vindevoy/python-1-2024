from itertools import combinations

START_SITUATION = {
    "left_people": [1, 2, 5, 10],
    "right_people": [],
    "time_spent": 0,
}


def get_move_to_right_combinations(situation):
    return list(combinations(situation["left_people"], 2))


def move_two_persons_to_right(situation, person1, person2):
    situation["left_people"].remove(person1)
    situation["left_people"].remove(person2)
    situation["right_people"].append(person1)
    situation["right_people"].append(person2)
    situation["time_spent"] += max(person1, person2)
    return situation


def get_move_to_left_combinations(situation):
    return situation["right_people"]


def move_one_person_to_left(situation, person):
    situation["right_people"].remove(person)
    situation["left_people"].append(person)
    situation["time_spent"] += person
    return situation


def main():
    situation = START_SITUATION.copy()
    situations = [situation]
    for situation in situations:
        situations.append(move_two_persons_to_right(situation.copy(), 1, 2))
        situations.remove(situation)
    for situation in situations:
        situations.append(move_one_person_to_left(situation.copy(), 1))
        situations.remove(situation)
    print(situations)


if __name__ == "__main__":
    main()
