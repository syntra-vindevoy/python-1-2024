d = {}

d["name"] = "John"
d[0] = "jhn"
d["names"] = ["jean", "jacques"]

print(d)

print (d["names"])
print ("The key name exists", "name" in d)
print ("The key Names exist", "Names" in d)

lst = [1, 2, 3]
# d = dict(lst) dit werkt niet
d = {i:lst[i] for i in range (len(lst))}
print (d)

# volgende overloopt heel de dict, is niet echt de bedoeling doit te gebruiken
for k in d:
    print (k, d[k])

print (d.keys())
print (d.values())

known = {0:0, 1:1}

def fibonacci_memo(n):
    if n in known:
        return known[n]

    res = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    known[n] = res
    return res

print(fibonacci_memo(5))

