t = [1, 2, 3, 4]
print(t)

def chop(l:list) -> None:
    del l[0]
    del l[-1]

chop(t)
print(t)
