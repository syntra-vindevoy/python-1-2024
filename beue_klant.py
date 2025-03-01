yves = {"naam": "yves", "stad": "oudenaarde"}
chiel = {"naam": "chiel *", "stad": "eksaarde"}
tom = {"naam": "tom **", "stad": "zottegem"}


persons = [yves, chiel, tom]

#def lmbd(x):
    #return x["naam"]

persons.sort(key=lambda x: x["naam"].count("*"), reverse=True) #, reverse=True)
#persons.sort(key=lambda x: "*" in ["naam"], reverse=True) #, reverse=True)


print(persons)