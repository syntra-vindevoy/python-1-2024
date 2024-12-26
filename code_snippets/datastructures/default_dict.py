from collections import defaultdict

# Define a set of keys
keys = {'a', 'b', 'c'}

# Create a defaultdict with a default value of 1
default_dict = defaultdict(int) # default value is 0
default_dict = defaultdict(lambda: 1)

# Initialize the defaultdict with the keys from the set
for key in keys:
    default_dict[key]

# Now default_dict has keys from the set with default values as 1
print(default_dict)