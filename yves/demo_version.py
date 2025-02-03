def version_part(s: str):
    if s.isnumeric():
        return int(s), s
    else:
        return 0, s

def version_is_newer(old_version, new_version):
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

    return new_version > old_version


import re

import re


import re


import re


def version_check(old_version, new_version):
    # Define the semantic ordering for known pre-release keywords
    pre_release_order = {
        "snapshot": 3,  # Higher number means newer
        "alpha": 2,
        "beta": 4,
        "milestone": 1,
        "rc": 5,  # Release Candidate
        "final": 6  # Final release is the newest
    }

    def normalize_version(version):
        # Ensure the input is a string
        version = str(version)
        # Use regex to extract parts (numbers or non-numeric segments)
        parts = re.findall(r'(\d+|[^\d.]+)', version)
        normalized = []
        for part in parts:
            if part.isdigit():
                # Convert numeric parts to integers
                normalized.append(int(part))
            else:
                normalized.append(
                    # Use semantic ordering for known pre-release tags
                    pre_release_order.get(part.lower(), part.lower())
                )
        return tuple(normalized)

    # Normalize both versions for comparison
    old_parts = normalize_version(old_version)
    new_parts = normalize_version(new_version)

    # Compare the normalized tuples lexicographically
    return new_parts > old_parts

if __name__ == "__main__":
    assert version_check(1, 2)
    assert version_check(1.0, 2.0)

    assert version_check("1.0", "2.0")
    assert version_check("3.0", "11.0")
    assert version_check("3.0", "11.0.0")

    assert version_check("1.0.0", "1.0.1")
    assert version_check("1.0.2", "1.0.10")

    assert version_check("1.a", "1.b")
    assert version_check("1.b", "2.a")

    assert version_check("1.0", "1.0_alpha")
    assert version_check("1.0.snapshot", "1.0.milestone")
