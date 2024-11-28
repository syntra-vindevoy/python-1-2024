c = ["cheddar","brie","gouda","stilton"]

print(c)

d = c
e = c.copy()  #maakt een copy op een nieuwe geheugen plek. als dan c gewijzigd wordt, dan blijft e ongewijzigd

c.append("parmesan")

print(c)
print(len(c))

print(d)   #d verwijst naar de lijst c, die aangepast is, dus gaat de volledige lijst zetten bij opvragen.
print(e)