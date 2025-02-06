cheeses = []

print(len(cheeses))
print(type(cheeses))

cheeses = ['Cheddar','Edam', 'Gouda']

print(len(cheeses))

print(cheeses[1])

cheeses[1] = 'Parmesan'

print(cheeses)

cheeses[1] = 'Edam'

print(cheeses)


s = 'spam'
t = list(s)

print(t)

s ='dit is een test met een zin'
t = s.split()

print(t)

s ='dit is een - test met een zin'
t = s.split('-')

print(t)

for cheese in cheeses:
    print(cheese)


