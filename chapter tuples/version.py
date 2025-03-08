#
# def version_part(s:str):
#     if s.isnumeric():
#         return int(s)
#     else: return 0, s
#
# def version_is_newer(old_version, new_version):
#     old_version = str(old_version)
#     old_version = tuple(i for i in old_version.split("."))
#     old_version = [version_part(v) for v in old_version ]
#     old_version = tuple(old_version)
#
#     new_version = str(new_version)
#     new_version = tuple(i for i in new_version.split("."))
#     new_version = [version_part(v) for v in new_version ]
#     new_version = tuple(new_version)
#
#     return new_version > old_version

import re


def version_is_newer(old_version, new_version):
    """
    Vergelijkt twee versies (strings, integers, of floats) door ze om te zetten naar tuples.
    Inclusief ondersteuning voor alfanumerieke delen zoals "1.1_alpha".

    Parameters:
    - old_version: De oude versie (str, int, of float).
    - new_version: De nieuwe versie (str, int, of float).

    Returns:
    - bool: True als new_version nieuwer is dan old_version, anders False.
    """

    def version_to_tuple(version):
        # Split de versie op punten, underscores en andere scheidingstekens
        parts = re.split(r'[._]', str(version))
        # Converteer elk deel naar een integer als dat mogelijk is, anders laat als string
        return tuple(int(part) if part.isdigit() else part for part in parts)

    # Zet beide versies om naar tuples
    old_tuple = version_to_tuple(old_version)
    new_tuple = version_to_tuple(new_version)

    # Vergelijk de tuples direct
    return new_tuple > old_tuple


if __name__ == '__main__':
    assert version_is_newer(2, 3) == True
    assert version_is_newer(1.0, 2.0) == True
    assert version_is_newer("1.0", "2.0") == True
    assert version_is_newer("2.0.0", "11.0.0") == True
    assert version_is_newer("1.0.0", "2.0.0") == True
    assert version_is_newer("1.0.2", "1.0.10") == True
    assert version_is_newer("1.a", "1.b") == True
    assert version_is_newer("1.1", "1.1_alpha") == True

a = "11.0.0"
print (tuple(a))
a = a.split(".")
print (a)
