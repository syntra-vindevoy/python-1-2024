# def mean(*args):
#     return sum(args) / len(args)
#
# #print(mean(1, 2, 3, 4, 5))
#
# t = [1, 2, 3, 4, 5]
# print(mean(*t))
#
# def toto(**kwargs):
#     for kw in kwargs:
#         print(f"{kw}: {kwargs[kw]}")
#
# print(toto(a=1, b=2, c=3))
#
# d = {'a': 1, 'b': 2, 'c': 3}
# print(toto(**d))

def version_part(s: str):
    if s.isnumeric():
        return int(s), s
    else:
        return 0, s

def version_is_newer(old_version, new_version):
    old_version = tuple(str(old_version).split("."))
    old_version = tuple(old_version)

    old_version = [version_part(v) for v in old_version]
    old_version = tuple(old_version)

    print(old_version)

    new_version = tuple(str(new_version).split("."))
    new_version = tuple(new_version)

    new_version = [version_part(v) for v in new_version]
    new_version = tuple(new_version)

    print(new_version)

    return new_version > old_version

    # return tuple(map(int, old_version.split("."))) < tuple(map(int, new_version.split(".")))

if __name__ == "__main__":
    assert version_is_newer(1, 2)
    assert version_is_newer(1.0, 2.0) == True
    assert version_is_newer("1.0", "2.0") == True
    assert version_is_newer("3.0", "11.0") == True
    assert version_is_newer("1.0.1" , "1.0.2") == True
    assert version_is_newer("1.0.1" , "1.0.10") == True
    assert version_is_newer("1.a" , "1.b") == True
    assert version_is_newer("2.b" , "3.c") == True
    assert version_is_newer("1.build_2", "1.build_10")
    assert version_is_newer("1.0", "1.0_alpha")