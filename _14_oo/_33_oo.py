from collections import namedtuple

# Dictionary representing a person's details
# - The keys in this dictionary are 'name', 'age', and 'country'
# - The values represent the corresponding details for this specific person
# - This structure is useful for storing data in a simple and flexible way
person = {"name": "John", "age": 36, "country": "Norway"}

# Creating a named tuple class 'PersonTuple' with fields: name, age, and country
# - Named tuples allow us to access stored data through both dot notation (e.g., p.name)
#   and index-based access (e.g., p[0]), making them more readable and convenient.
PersonTuple = namedtuple("PersonTuple", "name, age, country")

# Converting the `person` dictionary into a named tuple
# - The double asterisks (**) are used to unpack the dictionary's key-value pairs
#   into arguments for the named tuple's constructor.
# - After unpacking, the named tuple will hold the same data as the dictionary,
#   but will allow attribute-style access (e.g., p.name).
p = PersonTuple(**person)

# Accessing and printing the 'name' value using the dictionary approach
# - Accessing the value for the key 'name' directly from the dictionary
print(person["name"])

# Accessing and printing the 'name' value using the named tuple
# - Accessing the value through an attribute (dot notation)
print(p.name)


q = PersonTuple(name="Jane", age=25, country="United States")
q_person = q._asdict()
print(q_person)