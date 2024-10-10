yves = {"naam": "Yves", "stad": "Oudenaarde"}
chiel = {"naam": "Chiel *", "stad": "Eksaarde"}
tom = {"naam": "Tom *", "stad": "Zottegem"}


persons = [yves, chiel, tom]

persons.sort(key=lambda x: "*" in x["naam"], reverse=True)


print(persons)