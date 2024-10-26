def generate_all_combinations():
    # mistake in logic, one person can return more than one time, potential solutions missing...
    base = [1, 2, 5, 10]
    solutions = []
    for person1 in base:
        for person2 in base:
            for person3 in base:
                for person4 in base:
                    if (
                        person1 != person2 != person3 != person4
                        and person1 != person3
                        and person2 != person4
                        and person1 != person4
                    ):
                        solutions.append((person1, person2, person3, person4))
    return solutions


def calculate_time_spent(person1, person2, person3, person4):
    time_spent = 0
    time_spent += max(person1, person2)
    time_spent += person2
    time_spent += max(person2, person3)
    time_spent += person3
    time_spent += max(person3, person4)
    return time_spent


def main():
    list_combinations = generate_all_combinations()
    list_times_per_combination = []

    for combination in list_combinations:
        time_spent = calculate_time_spent(*combination)
        list_times_per_combination.append([time_spent, combination])

    list_times_per_combination = sorted(list_times_per_combination, key=lambda x: x[0])

    for i in list_times_per_combination:
        print(i)


if __name__ == "__main__":
    main()
