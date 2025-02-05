# Create a list of cheese types
c = ["cheddar", "parmesan", "brie", "feta"]

# Print the initial list of cheeses
print(c)

# Assign the list `c` to a new variable `d`
# Both `c` and `d` now point to the same mutable list in memory
d = c

# Create a shallow copy of the list `c` and assign it to `e`
# Changes to `c` will not affect `e`
e = c.copy()

# Append a new cheese, "mozzarella", to the list `c`
# This modification also impacts `d` since both reference the same list
c.append("mozzarella")

# Print the modified list `c` after adding "mozzarella"
print(c)

# Print the number of items in the list `c`
print(len(c))

# Print `d`, which reflects the same changes as `c`
print(d)

# Print `e`, which remains unchanged because it's a independent copy of the original `c` list
print(e)
