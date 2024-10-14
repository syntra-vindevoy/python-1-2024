# Zonder return r kunnen we niets berekenen, uitkomst code is None.
# Bij return r is de uitkomst 3.
from functools import reduce


def toto(a, b):
    r = a + b

print(toto(1,2))

#Lijst printen zonder return.
# lst = [1,4,7,2,2,9]
# lst = lst.sort()
#
# print(lst)

lst = [1,4,7,2,2,9]
lst = lst.sort()

print(lst)


# Andere fouten die mogelijk kunnen gemaakt worden.
# lst = [1,4,7,2,2,9]
#
# for l in lst.sort():
#     print(l)
# print(lst)

# ##
# lst = [1,4,7,2,2,9]
#
# for l in lst.sort():
#     print(l)
# print(lst)
# ##

lst = [1,4,7,2,2,9]
lst.sort()

for l in lst:
    print(l)

print(lst)


