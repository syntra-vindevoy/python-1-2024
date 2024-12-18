from collections import Counter, namedtuple, OrderedDict,defaultdict,deque

words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
counter = Counter(words)
print(counter)


words = "The quick brown fox jumps over the lazy dog"
counter = Counter(words)
print(counter)
for letter, count in counter.items():
    print(f"{letter}: {count}")


print(counter.most_common(3))
print(counter.most_common(3)[0][0])
print(counter.most_common(3)[0][1])

print(counter.most_common(3)[-1][0])

point= nectar = namedtuple('point', 'x, y')
pta = point(x=11, y=22)
print(pta)

print(pta.x)
print(pta.y)

#old python
dict_ord= OrderedDict()
dict_ord['c'] = 3
dict_ord['d'] = 4
dict_ord['a'] = 1
dict_ord['b'] = 2
dict_ord['e'] = 5


print(dict_ord)


default_dict = defaultdict(int)
default_dict['a'] += 1
default_dict['b'] += 1
default_dict['c'] += 1
print(default_dict['r']) # no error


d =deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(4)
print(d)

d.extendleft([5,6,7])
d.extend([8,9,10])
print(d)

p=d.pop()
l=d.popleft()
print(d)
print(p,l)

d.rotate(2)
print(d)



