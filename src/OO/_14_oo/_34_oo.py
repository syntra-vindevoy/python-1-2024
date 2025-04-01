# A list of dictionaries representing customers.
# Each dictionary contains customer details: "name", "address", and "age".
customers = [{"name": "John", "address": "123 Main street", "age": 30},
             {"name": "Jane", "address": "456 Main street", "age": 25},
             {"name": "John", "address": "789 Main street", "age": 20}]


# Define a lambda function that extracts the "name" key from a dictionary.
# This function is used for sorting by the "name" key.
def my_lambda(x):
    return x["name"]


# Sorting the customers list by the "name" key using a lambda function.
# NOTE: The `sort` method sorts the list in place and always returns `None`.
print(customers.sort(
    key=lambda x: x["name"]))  # This prints `None` because `sort` modifies the list in place.

# Sorting the customers list by "name" key again.
customers.sort(key=lambda x: x["name"])
# Now, the customers list is sorted alphabetically by the "name" key.
print(customers)


# Define another lambda function that returns a tuple of ("name", "age").
# This allows sorting in a two-level hierarchy: first by "name" and then by "age".
def my_lambda(x):
    return x["name"], x["age"]


# Sorting the customers list by a tuple consisting of "name" and "age".
# The tuple ensures customers with the same "name" are further sorted by "age" in ascending order.
customers.sort(key=lambda x: (x["name"], x["age"]))
# The final sorted list is printed, based on both "name" and "age".
print(customers)



# Initialize a list of integers.
lst = [1, 2, 3, 4, 5]

# Use the built-in `map` function with a lambda function to process the list.
# The lambda function takes each element `x` from the list and multiplies it by 2.
# `map` applies this transformation to all elements of the list.

# The `map` function returns a map object (an iterator), so we wrap it with `list()`
# to convert the result to a list of doubled values.
print(list(map(lambda x: x * 2, lst)))

# Output: [2, 4, 6, 8, 10]
