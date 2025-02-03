def mean(*args):
    return sum(args) / len(args)


t = [1, 2, 3, 4, 5]
print(mean(*t))


def toto(**kwargs):
    for kw in kwargs:
        print(f"{kw}: {kwargs[kw]}")


print(toto(a=1, b=2, c=3))

d = {"a": 1, "b": 2, "c": 3}
print(toto(**d))


def homepage(request, *args, **kwargs):
    pass
