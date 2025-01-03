mytupel= ("one two three four five six seven eight nine ten",)

print(mytupel)

mytupel2= ("one two three four five six seven eight nine ten",1,2,3,4,5,6,7,8,9,10,"fdfdsfdsfsd")
mytupel2= mytupel2 + (11,12,13,14,15)

print(mytupel2)

mytupel3= tuple(range(1,11))
print(mytupel3)

for i in mytupel3:
    print(i)


ret = [i for i in mytupel2 if isinstance(i, str)]
print(ret)

print(mytupel2.index(2))

print(mytupel2[2:5])