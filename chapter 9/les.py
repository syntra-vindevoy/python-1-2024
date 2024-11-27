cheeses = ["Cheddar", "Edam", "Gouda"]

print(cheeses[1:])
print (cheeses[0:2])
print (cheeses[1:3])
print (cheeses[:2])
print (cheeses[1::-1])
print (cheeses[0::2])
print (cheeses[:1:-1])
print (", ".join(cheeses))
print (", ".join(cheeses[1:]))

ip = "192.168.0.80"
print (ip.split("."))
ip_2 = ["192", "168", "0", "80"]
f = ".".join(ip_2)
print(f)

s = "pining for the fjords"

for word in s.split():
    print(word)

#cheeses = sorted (cheeses)
#print(cheeses)

cheeses.sort()
print(cheeses)

a = "fg"
b = "fg"
print (a is b)

a = [5,8,9,7,]
a[1] = 10
print(a)