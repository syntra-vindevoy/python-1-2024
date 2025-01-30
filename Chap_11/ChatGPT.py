# def version_is_check(old_version, new_version):
#     return new_version > old_version



def version_is_check1(old_version, new_version):
    def parse_version(version):
        # Ensure all parts are strings and ensure numeric parts use zero-padded length for proper comparison
        return [
            part.zfill(10) if part.isdigit() else part
            for part in str(version).split(".")
        ]

    # Compare the parsed versions by converting numeric segments and proper lexicographical handling
    return parse_version(old_version) < parse_version(new_version)

if __name__ == "__main__":
# Updated tests
    assert version_is_check1("3.0", "11.0") == True  # Should pass
    assert version_is_check1(1, 2)  # Numbers-only comparison
    assert version_is_check1("1.0.1", "1.0.2") == True
    assert version_is_check1("1.0.1", "1.0.10") == True
    assert version_is_check1("1.a", "1.b") == True  # Non-numeric parts compared lexicographically
    assert version_is_check1("2.b", "3.c") == True  # Non-numeric parts compared lexicographically
    assert version_is_check1("1.0.a", "1.0.b") == True  # Mixed parts compared successfully
    assert version_is_check1("10.0", "2.0") == False  # Ensure padded sorting works
    assert version_is_check1("1.0", "1.0_alpha") == True  # Lexicographical comparison works
    assert version_is_check1("1.0.snapshot", "1.0.milestone") == False
    assert version_is_check1("1.0.milestone", "1.0.snapshot") == True
    assert version_is_check1("1.0.rc", "1.0.snapshot") == True
    assert version_is_check1("1.0.snapshot", "1.0.rc") == False