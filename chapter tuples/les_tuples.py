x = ()
#dit zijn tuples, met op zonder haakjes
x = (1,2)
y = 1, 2
print(type(x))
print(type(y))

a = 1
b = 2
a, b = b, a
print(a, b)

a = 1
b = 2
c = (a, b)

t = tuple("hallo") #breekt alle waardes op in een tuple
t = ("hallo",) #zonder de komma is het geen tuple
print (t)
print (sorted(t))

t = (1,2,"h", [1,2,3])
#print (sorted(t)) #werkt niet, kan dit niet sorteren

a, b = 5, 6
print (a)
print (b)

a = 1.5 # is float
a = 1,5 # is tuple
print (a)

a, b, _ = 1, 5, 6 # _ toevoegen als waarde niet gebruikt wordt
print (a,b)

email = 'monty@python.org'
username, domain = email.split('@')

d = {'one': 1, 'two': 2}

for item in d.items():
    key, value = item
    print(key, '->', value)

def mean(*args):
    return sum(args)/len(args)
print(mean(1,5,8,9))

t = [1,8,9,7]
print(mean(*t))

def toto(**kwargs):
    for kw in kwargs:
        print (f"{kw} : {kwargs[kw]}")
toto(a=1, b=2, c=3)

d = {'a': 1, 'b': 2, 'c': 3}
toto(**d)

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))
print (letter_map)