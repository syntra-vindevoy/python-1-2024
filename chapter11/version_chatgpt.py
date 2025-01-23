def version_is_newer(old_version, new_version):
    """
    Compare two version numbers.
    Returns True if new_version is newer than old_version, otherwise False.

    Args:
        old_version (int, str, list): The older version.
        new_version (int, str, list): The newer version.

    Returns:
        bool: True if new_version is newer, False otherwise.
    """
    # Convert both versions to strings if they aren't already
    old_version = str(old_version)
    new_version = str(new_version)

    # Split versions by dots to compare subversions and convert to tuples
    def parse_version(version):
        parsed = []
        for part in version.split('.'):
            if part.isdigit():
                parsed.append((int(part), ""))  # Numeric parts are tuples with an empty string
            else:
                parsed.append((0, part))  # Non-numeric parts have 0 as the numeric value
        return tuple(parsed)

    old_version_tuple = parse_version(old_version)
    new_version_tuple = parse_version(new_version)

    # Compare tuples directly
    return new_version_tuple > old_version_tuple


if __name__ == "__main__":
    assert version_is_newer(1, 2) == True
    assert version_is_newer(1.0, 2.0) == True

    assert version_is_newer("1.0", "2.0") == True
    assert version_is_newer("3.0", "11.0") == True
    assert version_is_newer("1.0.0", "1.0.1") == True
    assert version_is_newer("1.0.2", "1.0.10") == True

    assert version_is_newer("1.a", "1.b") == True
    assert version_is_newer("1.0", "1.0_alpha") == True
    assert version_is_newer("3.0", "11.0.0") == True