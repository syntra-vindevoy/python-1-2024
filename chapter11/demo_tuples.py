# tuple start met ronde haakjes
z = () # zo maken we een lege tuple aan

x = (1, 2)
y = 1, 2
# stilzwijgend is y ook een tuple, een variabele met een , zonder ronde haken hoort ook tot de classe tuple

print(type(x))
print(type(y))
print(type(z))

a = 1
b = 2
# probeer de waarde van b in a te krijgen, en a in b

a, b = b, a  # is gelijk aan a, b = (b, a)
# tuple kan gebruikt maken als 3de item
#bovenstaande gaat een tuple aanmaken, met b en a als waarde. hij copiëert deze waardes, geen verwijzingen.
#de waardes zitten dus in memory.

#y = ('yves') #voor dit gaat hij klagen. want dit is eigenlijk geen tuple, maar gewoon een verwijzing van een variabbele aan ee nstring
#y = ('yves', ) door de comma erbij is dit dan weer wel een tuple, een tuple verwijst dus minimum 1 comma

a = tuple('Yves')  #deze functie gaat de string gaan opsplisen
print(a)

print(sorted(tuple('Yves')))

#11.2 tuples zijn immutable
# die moeten dus volledig verwijderd worden als ge dezelfde wilt opnieuw maken/aanpassen
# een tuple aanpassen, is in sé een nieuwe tuple aanmaken.

#tupple assignments
a, b = 1, 2
print(a)

#a, b = 1, 2, 3  # dit gaat een error geven, want je geeft 1 waarde teveel mee.
#dit lossen we op door een underscore aan toe te voegen
d, e, _ = 1, 2, 3  # per variabele dat niet gebruikt wordt, moet er een _ gezet worden.
print(_)  # die _ moeten we echt zien als variabele. dit wordt wel gezien als 1 die niet gebruikt wordt.

#11.5 argument packaging

def mean(*args ):  # de ster + args zorgt ervoor dat alles wat er staat in een tuple komt, kunnen dus oneindig argumenten toegevoegd worden. (kwargs, key and value)
    return sum(args)/len(args)
#voorbeeld van een functie zoals bovenaan, de print functie

print(mean(1, 2, 3, 4, 5))

g = [1, 2, 3, 4, 5]
#print(mean(g)) # dit gaat niet lukken, want hij krijgt een lijst die hij neit kan verwerken
print(mean(*g)) #het sterretje daarentegen zorgt ervoor dat de items in de lijst allemaal afzonderlijk in functie gaan komen

def toto(**kwargs): # key arguments, 2 sterretjes zorgt er voor dat er meerdere keyvalue pairs mogen toegevoegd worden
    for kw in kwargs:
        print(f"{kw}: {kwargs[kw]}")

print(toto(a=1, b=2, c=3))

h = {"a": 1, "b": 2, "c": 3}
print(toto(**h))

#11.6. zip
#dit gaat 2 tuples in elkaar zippen zoals een tirret. 1ste van tuple 1, 1ste van tuple 2, 2de van tuple 1....

## 11.7 comparing en sorting (dit is waarom tuples zo leuk zijn)
# in bijna elk geval kan je een tuple sorteren
def version_part(s: str):
    if s.isnumeric():
        return int(s), s
    else:
        return 0, s

def version_is_newer(old_version, new_version):
    #1old_version = str(old_version).split('.')
    #1new_version = str(new_version).split('.')

    #1old_version = [int(v) for v in old_version]
    #1old_version = tuple(old_version)

    #1new_version = [int(v) for v in new_version]
    #1new_version = tuple(new_version)

    old_version = str(old_version).split('.')
    old_version = tuple(old_version)

    old_version = [version_part(v) for v in old_version]
    old_version = tuple(old_version)
    #print(old_version)

    new_version = str(new_version).split('.')
    new_version = tuple(new_version)

    new_version = [version_part(v) for v in new_version]
    new_version = tuple(new_version)
    #print(new_version)

    return tuple(old_version) < tuple(new_version)

if __name__ == "__main__":
    assert version_is_newer(1, 2) == True
    assert version_is_newer(1.0, 2.0) == True

    assert version_is_newer("1.0", "2.0") == True
    assert version_is_newer("3.0", "11.0") == True
    assert version_is_newer("1.0.0", "1.0.1") == True
    assert version_is_newer("1.0.2", "1.0.10") == True

    assert version_is_newer("1.a", "1.b") == True
    assert version_is_newer("1.0", "1.0_alpha") == True