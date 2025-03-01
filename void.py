def toto (a, b):
    r = a + b

print(toto(1, 2))

#resultaat is None omdat er geen return bij staat
#void function

lst = [1, 4, 7, 2]
#lst = lst. sort() #function method

#oplossing
#lst = sorted(lst)
lst.sort() #oplossing

for l in lst:
    print(l)

print(lst)
