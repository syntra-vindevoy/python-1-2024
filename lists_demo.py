from numpy import mean

cheeses = ["cheddar", "edam", "gouda"]

#print(cheeses[1::-1])

print(",".join(cheeses[:2]))


t1 = [1, 2, 3]
t2 = [4, 5, 6]

t1.append(t2)

print(t1)

t1 = [1, 2, 3]
t1.extend(t2)

print(t1)

print(t1 * 2)

t1 = [1, 2, 3, 4, 5, 6]
t2 = [4, 5, 6]

t3 = set(t1) - set(t2)

print(list(t3))

print(sum(t1))

print(mean(t1))

print(avgpp(t1))

print(median(t1))

t.pop(1,)
t1.remove(1)
print(t1)
print(t1[5])

ip = "192.168.0.180"
print(ip.split("."))
print(s.split())
