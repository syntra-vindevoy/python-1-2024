# def mean(*args):
#     return sum(args) / len(args)
#
# print(mean(1, 2, 3, 4, 5))
#
# t =[1, 2, 3, 4, 5]
# print(mean(*t))
#
# def toto(**kwargs):
#     for kw in kwargs:
#         print(f"{kw}: {kwargs[kw]}")
#
# print(toto(a=1, b=2, c=3))
#
# d = {"a": 1, "b": 2, "C": 3}
# print(toto(**d))

def version_part(s: str):
    if s.isnumeric():
        return int(s), s
    else:
        return 0, s

def version_is_newer(old_version, new_version):

    """
    Compare if the new_version is newer than the old_version.

    Args:
        old_version (str, int, float): The old version (e.g., "1.2.3", 1, 1.0).
        new_version (str, int, float): The new version (e.g., "1.3.0", 2, 2.0).

    Returns:
        bool: True if new_version is newer than old_version, False otherwise.
    """
    # Split versions into parts
    old_version_parts = tuple(int(part) if part.isdigit() else part for part in str(old_version).split("."))
    new_version_parts = tuple(int(part) if part.isdigit() else part for part in str(new_version).split("."))

    # Compare versions
    return new_version_parts > old_version_parts

def version_is_newer3(old_version, new_version):
    return tuple(int(part) if part.isdigit() else part for part in str(old_version).split(".")) < tuple(
        int(part) if part.isdigit() else part for part in str(new_version).split("."))

import re

def version_is_newer4(old_version, new_version):
    """
    Compare if the new_version is newer than the old_version.

    This version uses regular expressions to handle splitting of the version strings.

    Args:
        old_version (str, int, float): The old version.
        new_version (str, int, float): The new version.

    Returns:
        bool: True if new_version is newer than old_version, False otherwise.
    """

    def parse_version(version):
        # Split version by anything that's not a digit or alphabetic character
        parts = re.split(r'[\D]', str(version))
        return tuple(int(p) if p.isdigit() else p for p in parts if p)

    # Parse both versions
    old_version_parsed = parse_version(old_version)
    new_version_parsed = parse_version(new_version)

    # Compare versions
    return new_version_parsed > old_version_parsed


def version_is_newer2(old_version, new_version):


    old_version = str(old_version).split(".")
    old_version = tuple(old_version)

    old_version = [version_part(v) for v in old_version]
    old_version = tuple(old_version)
    #print(old_version)

    new_version = str(new_version).split(".")
    new_version = tuple(new_version)

    new_version = [version_part(v) for v in new_version]
    new_version = tuple(new_version)
    #print(new_version)


    # old_version = [int(v) for v in old_version]
    # old_version = tuple(old_version)
    # print(old_version)
    #
    # new_version = str(old_version).split(".")
    # new_version = [int(v) for v in old_version]
    # new_version = tuple(old_version)
    # print(new_version)

    return new_version > old_version

def main():

    assert version_is_newer(1, 2)
    assert version_is_newer(1.0, 2.0)

    assert version_is_newer("1.0", "2.0")
    assert version_is_newer("3.0", "11.0")

    assert version_is_newer("1.0.0", "1.0.1.0")
    assert version_is_newer("1.0.2", "1.1.10")

    assert version_is_newer("1.2.3.a","1.2.3.b")


if __name__ == "__main__":
    main()