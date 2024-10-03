#Global Variables

from global_strings import APPLICATION_NAME

a = 2

def f():
    global a                    #Not possible to assign value gere

    a = 3

f()

print(a)
print(APPLICATION_NAME)
