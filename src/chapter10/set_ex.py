set_a = set()
set_a.add(1)
set_a.add(2)
set_a.add(3)
print(set_a)
for i in set_a:
    print(i,end=" ")

if 1 in set_a:
    print("1 in set_a")

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

print(odds.union(evens))
print(odds.intersection(evens))
print(odds.difference(evens))
print(odds.symmetric_difference(evens))
print(primes.issubset(odds))
print(primes.issuperset(odds))

print(odds.isdisjoint(evens))
print(odds.isdisjoint(primes))

odds.add(11)
odds.remove(3)
print(odds)
odds.update([13,15])
print(odds)
