
def version_is_newer1(old_version, new_version):
    return new_version > old_version


def version_is_newer2(old_version, new_version):
    return float(new_version) > float(old_version)


def version_is_newer3(old_version, new_version):
    old_version = str(old_version).split(".")
    old_version = [int(v) for v in old_version]
    old_version = tuple(old_version)

    new_version = str(new_version).split(".")
    new_version = [int(v) for v in new_version]
    new_version = tuple(new_version)

    return new_version > old_version

def version_part(s:str):
    if s.isnumeric():
        return int(s), s
    else:
        return 0, s

def version_is_newer4(old_version, new_version):
    old_version = str(old_version).split(".")
    old_version = tuple(old_version)

    old_version = [version_part(v) for v in old_version]
    old_version = tuple(old_version)
    print(old_version)

    new_version = str(new_version).split(".")
    new_version = tuple(new_version)

    new_version = [version_part(v) for v in new_version]
    new_version = tuple(new_version)
    print(new_version)

    return new_version > old_version


def version_is_newer(old_version, new_version):
    """
    Compares two version strings to determine if the `new_version` is newer than `old_version`.

    Handles both numeric and alphanumeric segments in versioning (e.g., 1.0 and 1.0_alpha).
    """
    # Split the version strings into segments by "."
    old_parts = [version_part(part) for part in str(old_version).split(".")]
    new_parts = [version_part(part) for part in str(new_version).split(".")]

    # Compare the two lists of parts segment by segment
    return new_parts > old_parts


if __name__ == "__main__":
    assert version_is_newer(1, 2) == True
    assert version_is_newer(1.0, 2.0) == True

    assert version_is_newer("1.0", "2.0") == True
    assert version_is_newer("3.0", "11.0") == True

    assert version_is_newer("1.0.0", "1.0.1") == True
    assert version_is_newer("1.0.2", "1.0.10") == True

    assert version_is_newer("1.a", "1.b") == True
    assert version_is_newer("2.a", "2.b") == True

    assert version_is_newer("1.0", "1.0_alpha") == True