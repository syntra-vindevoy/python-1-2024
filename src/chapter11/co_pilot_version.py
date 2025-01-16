def is_version_less_than(current_version, new_version):
    def parse_version(version):
        if isinstance(version, int):
            return [version]
        elif isinstance(version, str):
            return [int(part) if part.isdigit() else part for part in version.replace('_', '.').split('.')]
        else:
            raise ValueError("Unsupported version type")

    current_parts = parse_version(current_version)
    new_parts = parse_version(new_version)

    for c, n in zip(current_parts, new_parts):
        if isinstance(c, int) and isinstance(n, int):
            if c < n:
                return True
            if c > n:
                return False
        elif isinstance(c, str) and isinstance(n, str):
            if c < n:
                return True
            if c > n:
                return False
        else:
            return isinstance(c, str) and not isinstance(n, str)

    return len(current_parts) < len(new_parts)

# Test cases
assert is_version_less_than(1, 2) == True
assert is_version_less_than(2, 1) == False
assert is_version_less_than("1.0", "1.1") == True
assert is_version_less_than("3.0", "11.0") == True
assert is_version_less_than("1.0.0", "1.1.0") == True
assert is_version_less_than(5, "6.0") == True
assert is_version_less_than("7.5", 8) == True
assert is_version_less_than("7.a", "8.b") == True
assert is_version_less_than("7.0_alpha", "8.0") == True
