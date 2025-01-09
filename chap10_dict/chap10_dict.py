d = {}
d = dict()

d["name"] = "John"
d["0"] = "jkl"
d["names"] = ["Thomas", "Mary", "Jane"]

print(d)

d["name"] = "Yves"      #Replace value of key
print(d)

#print(d["Name"])       Dict is case sensitive
print(d["name"])

print("The key Name exists: ", "name" in d)
print("The key Name exists: ", "Name" in d)

lst = ["Thomas", "Mary", "Jane"]
d = {i:lst[i] for i in range(len(lst))}

print(d)

for k in d:
    print(k, d[k])

print(d.keys())
print(type(d.keys()))
print(d.values())