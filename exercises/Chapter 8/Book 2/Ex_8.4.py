def any_lowercase1(s): #only returns value of 1 character
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower(): #'c' is verkeerd moet gewoon c zijn.
            return 'True'
        else:
            return 'False'

def any_lowercase3(s): #gaat True of False terug geven afhankelijk of het eerste character een groot of kleine letter heeft
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s): #vanaf er 1 character lower is word er niet meer geupdate
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s): #vanaf er 1 character hoger is geeft funtie false terug anders waar.
    for c in s:
        if not c.islower():
            return False
    return True

s = 'bAnana'
print(any_lowercase1(s))
print(any_lowercase2(s))
print(any_lowercase3(s))
print(any_lowercase4(s))
print(any_lowercase5(s))
