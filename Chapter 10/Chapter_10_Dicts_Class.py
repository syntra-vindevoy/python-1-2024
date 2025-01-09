# d = {}
# d = dict()
# #print(d)
# d["name"] = "John"
# d[0] = "jkl"
#
# d["names"] = ["Yves", "Jaques"] #List in dict steken, geeft als resultaat {'name': 'John', 0: 'jkl', 'names': ['Yves', 'Jaques']}
# #print(d)
#
# #print(d["name"]) #Keys zijn hoofdlettergevoelig
#
# #print("The key name exists", "name" in d)
# #print("The key Name exists", "Name" in d)

lst = ["jksl", "oejr", 3]
d = {i: lst[i] for i in range(len(lst))}

print(d)