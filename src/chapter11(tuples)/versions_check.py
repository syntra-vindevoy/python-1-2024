def convert_non_numeric(part):
  """Converts a non-numeric part of a version string to an integer for comparison.

  Args:
    part: The non-numeric part of the version string.

  Returns:
    An integer representation of the part.
  """
  try:
    return int(part)
  except ValueError:
    # If the part is not an integer, assign a large value to ensure it's treated as greater
    return 10000  # Or another sufficiently large value

def is_version_less_than(current_version, new_version):
  """
  Checks if the current_version is less than the new_version.

  Args:
    current_version: The current version string.
    new_version: The new version string.

  Returns:
    True if current_version is less than new_version, False otherwise.
  """
  try:
    # Attempt to convert both versions to integers
    current_version = int(current_version)
    new_version = int(new_version)
    return current_version < new_version
  except ValueError:
    # If conversion to integers fails, proceed with string comparison
    current_version_parts = [convert_non_numeric(part) for part in str(current_version).split('.')]
    new_version_parts = [convert_non_numeric(part) for part in str(new_version).split('.')]

    for i in range(min(len(current_version_parts), len(new_version_parts))):
      if current_version_parts[i] < new_version_parts[i]:
        return True
      elif current_version_parts[i] > new_version_parts[i]:
        return False

    return len(current_version_parts) < len(new_version_parts)

# Assertions to test the function
assert is_version_less_than(1, 2) == True
assert is_version_less_than(2, 1) == False
assert is_version_less_than("1.0", "1.1") == True
assert is_version_less_than("3.0", "11.0") == True
assert is_version_less_than("1.0.0", "1.1.0") == True
assert is_version_less_than(5, "6.0") == True
assert is_version_less_than("7.5", 8) == True
assert is_version_less_than("7.a", "8.b") == True
assert is_version_less_than("7.0_alpha", "8.0") == True