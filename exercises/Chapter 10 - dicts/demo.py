from sortedcontainers import SortedDict

# aanmaken d als dict
d = {}
d = dict()

d["name"] = "John"
d[0] = "jkl"

d["names"] = ["Yves", "Jane"]
print(d)

print(d["name"])

# print("The key exists: ", "name" in d)
# print("The key exists: ", "Name" in d)

lst = [1,2,3]
d = {i: lst[i] for i in range(len(lst))} #omzetting van lijst naar dict

for k in d:         #Dict overlopen
    print(k, d[k])

points = {"Anderlecht":33, "Club Brugge": 41, "Genk": 42, "Antwerp": 32, "Union": 33}

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

rankings = SortedDict(invert_dict(points))
print(rankings)