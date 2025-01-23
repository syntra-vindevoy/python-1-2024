from sortedcontainers import SortedDict

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


points = {"Anderlecht": 33, "Club Brugge": 41, "Genk": 42, "Antwerp": 32, "Union": 33}
rankings = SortedDict(invert_dict(points))

print(rankings)