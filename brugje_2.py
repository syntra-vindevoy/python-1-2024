from itertools import combinations


situation = {"left": [1, 2, 5, 10], "right": [], "time_spent": 0}
situations = [situation]


comb = combinations(situation["left"], 2)


for situation in situations:
    for c in comb:

        new_situation = situation.copy()
        new_situation["left"] = [x for x in new_situation["left"] if x not in c]
        new_situation["right"] = list(c)
        new_situation["time_spent"] += max(c)
        situations.append(new_situation)
    print(situation)
