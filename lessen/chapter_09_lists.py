a = 5
b = a
a = 6
# print(a,b)
# 6,5


c = ["a", "b", "c"]
d = c
c.append("d")
print(c)
print(d)

print("copy")
e = c.copy()
c.append("e")
print(c)
print(e)

# slices
letters = ["a", "b", "c", "d", "e", "f", "g"]
# geen lijst
print(letters[2])  # c
# wel een lijst van zodra dubbel punten gebruikt worden
print(letters[2:5])  # ['c','d','e']
print(letters[:2])  # ['a','b']
print(letters[2:])  # ['c','d','e','f','g']
print(letters[:])  # ['a','b','c','d','e','f','g']
print(letters[:-2])  # ['a','b','c','d','e','f']
print(letters[-2:])  # ['f','g']
print(letters[::2])  # ['a','c','e','g']
print(letters[::-1])  # ['g','f','e','d','c','b','a']
# warning: slicing returntype is a list.

listname = ["a", "b", "c", "d", "e", "f", "g"]
last_item_in_list = listname[:1:-1]  # returnt list, geen item
last_item_in_list = listname[:1:-1][0]  # returnt item
print(", ".join(last_item_in_list))  # join functie om één item te krijgen

first_item_in_list = listname[0]

print("--------------------------------------")

t1 = [1, 2, 3]
t2 = [4, 5, 6]
t3 = t1 + t2
print(t3)
# zelfde als
extended_list = list.extend  # uitbreiden cfr T1+T2
# niet zelfde als
appended_list = list.append  # toevoegen

["spam"] * 3  # ['spam','spam','spam']
[1, 2, 3] * 3  # [1,2,3,1,2,3,1,2,3]
# opletten, lijst* is geen vermenigvuldiging, maar een uitbreiding van de lijst

t1 - t2  # error, geen aftrekking mogelijk

t3 = set(t1) - set(t2)  # {1,2,3} - {4,5,6} = {1,2,3}
# opletten: returnt een set, geen list
t3 = list(set(t1) - set(t2))  # [1,2,3]
# werkt wel, maar is niet efficiënt
# Efficient solution using list comprehension
t3 = [item for item in t1 if item not in t2]
print(t3)

sum_value = sum(t1)  # 6
min_value = min(t1)  # 1
max_value = max(t1)  # 3
print(numpy.mean(t1))  # 2.0 (som gedeeld door aantal)
print(avg(t1))  # 2.0 (som gedeeld door aantal)
print(median(t1))  # 2.0 (middenwaarde) (gemiddelde van twee middenste getallen)

t = [1, 2, 3]
pop_value = t.pop(1)  # verwijderd item op index 1
# pop verwijdert maar returnt ook de waarde
# verwijdert positie
t.remove(2)  # verwijderd item 2
# remove verwijdert maar returnt geen waarde, void functie
# verwijdert eerst matchende waarde
# waarde moet er in zitten of error


list("moehaha")  # ['m','o','e','h','a','h','a','h','a']
moehaha = "moehaha".split()  # ['m','o','e','h','a','h','a','h','a']
ip = "192.168.0.88"
ip_split = ip.split(".")  # ['192','168','0','88']

delimiter = "."
ip_join = delimiter.join(ip_split)  # 192.169.0.88
ip_join = ".".join(ip_split)  #

# loopen
for i in list:
    print(i)

for index in len(list):
    print(list[index])

# sorteren
t = ["d", "c", "e", "b", "a"]

# functie
sorted_list = sorted(t)  # ['a','b','c','d','e'] # void functie

# method
t.sort()  # ['a','b','c','d','e'] # voert sort uit op zichzelf

unsorted_list = ["d", "c", "e", "b", "a"]
unsorted_list = unsorted_list.sort()  # void functie, returnt None !!!

a = [1, 2, 3]
b = [4, 5, 6]

print(a is b)  # vergelijkt referentie
print(a == b)  # vergelijkt inhoud

# aliasing
a = [1, 2, 3]
b = a
b is a
