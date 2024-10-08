a = 2

from global_strings import APPLICATION_NAME

def f():
    global a

    a = 3


f()
print(a)
print(APPLICATION_NAME)
