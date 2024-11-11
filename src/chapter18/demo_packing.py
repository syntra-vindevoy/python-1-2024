def mean(*args, **kwargs):
    print(kwargs)
    return sum(args) / len(args)


def mean2(*args, **kwargs):
    return sum(args, **kwargs) / len(args)


def pack_and_print(**kwargs):
    print(kwargs)


pack_and_print(a=1, b=2)
assert mean(1, 2, 3, 4, 5) == 3
assert mean(1, 2, start=3) == 1.5

assert mean2(1, 2, 3, 4, 5, start=3) == 3.6

if __name__ == '__main__':
    print(mean(1, 2, 3, 4, 5))
    print(mean(1, 2, start=3))
    print(mean2(1, 2, 3, 4, 5, start=3))
