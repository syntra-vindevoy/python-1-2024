cheeses = ["cheddar", "parmesan", "feta"]
print(cheeses[1])                   #Type = String
print(cheeses[0:1])                 #Type = list
print(cheeses[0:2])                 #Type = list
print(cheeses[0:len(cheeses)])      #Type = list
print(cheeses[0:])                  #Type = list
print(cheeses[1:])                  #Type = list
print(cheeses[1::1])                #Type = list
print(cheeses[1::2])                #Element '3' doesn't exist so isn't printed
print(cheeses[1::-1])               #'-1' run backward
print(cheeses[:1:-1])               #'-1' run backward

test = ["a", "b", "c", "d", "e"]
print(test[:2:-1])



a = "banana"
b = "banana"
print(a is b)
print(a == b)

c = [1, 2, 3]
d = [1, 2, 3]
print(c is d)
print(c == d)

