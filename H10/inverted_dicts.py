from sortedcontainers import SortedDict

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]  # Ensure a list
        else:
            inverse[val].append(key)  # Add the key to the list
    return inverse

points = {"Anderlecht": 33, "Club Brugge": 41, "Genk": 41, "Antwerp": 32, "Union": 33}
rankings = SortedDict(invert_dict(points))

print(rankings)
