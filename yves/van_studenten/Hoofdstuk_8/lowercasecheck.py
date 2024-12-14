def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

print(any_lowercase1('Yes doctor Vandenberghe'))

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

print(any_lowercase3('Yes heel goeD'))

### ALLEEN LAATSTE LETTER CHECKEN

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
        return flag

print(any_lowercase4('YES dikken'))

### DEZE LIJKT GOED


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase5('YES dikken'))
