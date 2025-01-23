d = {}

d["name"] = "John"

d["0"] = "jkl"

d["names"] = ["jkl", "jacques"]

#print(d["name"])
#print("the key name exists", "name" in d) #key "name" bestaat in de dict
#print("the key name exists", "Name" in d) #key "name" bestaat niet in de dict

#print(len(d))  #geeft het aantal key values terug uit de dict

lst = ["dfdfe", "mijmikjmij", 3]
d = {i:i for i in range(len(lst))}
e = {i:lst[i] for i in range(len(lst))}
print(d)
print(e)

for k in d:
    print(k, d[k])


#inverted dicts
# hij gaat bij inverted dicts de key values omwisselen met de value
#dus value wordt dan uw key
#probleem: wat wanneer een waarde 2x voorkomt, zoals hieronder in het voorbeeld = 33
# bij het omwisselen, gaat hij dan de waarde als key opgeven, en elke key die bij die waarde hoort, dan mee opgeven in lijst
#onderstaande vb: wordt dan 33 ['anderlecht', 'union']




def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

from sortedcontainers import SortedDict

points = {"Anderlecht": 33, "Club Brugge": 41, "Genk": 42, "Antwerp": 32, "Union": 33}
rankings = SortedDict(invert_dict(points))



print(rankings)