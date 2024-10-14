yves = {"naam": "Yves", "stad":"Oudenaarde"}
chiel = {"naam": "Chiel *", "stad":"Eksaarde"}
tom = {"naam": "Tom **", "stad":"Zottegem"}


persons = [yves, chiel, tom]

#Hetzelfde functie op rij 13
# def lmbd(x):
#     return x ["naam"]

#Sorten op *
#persons.sort(key=lambda x: x ["naam"].count("*"), reverse=True)

persons.sort(key=lambda x: "*" in x ["naam"], reverse=True)

print(persons)


