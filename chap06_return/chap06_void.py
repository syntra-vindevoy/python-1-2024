#Void function, "returns" None
def my_func(a, b):
    r = a + b

print(my_func(1, 2))


lst1 = lst2 = [1, 4, 7, 2, 4, 9]
lst1 = lst1.sort()        #Lst will give None when printed, because the "return" of the sort is None
lst2.sort()               #Lst will sort the values inside and when printed, you get the sorted list values

print(lst1)
print(lst2)

for l in lst2:
    print(l)

lst3 = sorted(lst2)
print(lst3)