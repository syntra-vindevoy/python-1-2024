'''
In Python, an object is considered hashable if it has a hash value that remains constant during its lifetime. Hashable objects can be used as keys in dictionaries and as elements in sets because they can be compared for equality and their hash value can be computed.

### Hashable Objects
- **Immutable**: Hashable objects are typically immutable, meaning their state cannot be modified after they are created.
- **Examples**: 
  - **Numbers**: `int`, `float`
  - **Strings**: `str`
  - **Tuples**: Only if all elements within the tuple are also hashable
  - **Frozensets**: Immutable version of sets

### Unhashable Objects
- **Mutable**: Unhashable objects are typically mutable, meaning their state can be modified after they are created.
- **Examples**: 
  - **Lists**: `list`
  - **Dictionaries**: `dict`
  - **Sets**: `set`

### Why Hashability Matters
- **Dictionaries**: Keys in dictionaries must be hashable because the dictionary uses the hash value to quickly look up the key.
- **Sets**: Elements in sets must be hashable for the same reason, to ensure quick lookups and to maintain uniqueness.


### Example of Hashable and Unhashable Objects

'''

# Hashable examples
hashable_int = 42
hashable_str = "hello"
hashable_tuple = (1, 2, 3)
hashable_frozenset = frozenset([1, 2, 3])

# These can be used as dictionary keys or set elements
my_dict = {hashable_int: "value", hashable_str: "value", hashable_tuple: "value", hashable_frozenset: "value"}
my_set = {hashable_int, hashable_str, hashable_tuple, hashable_frozenset}

# Unhashable examples
unhashable_list = [1, 2, 3]
unhashable_dict = {"key": "value"}
unhashable_set = {1, 2, 3}

# These cannot be used as dictionary keys or set elements
# my_dict = {unhashable_list: "value"}  # TypeError: unhashable type: 'list'
# my_set = {unhashable_list}  # TypeError: unhashable type: 'list'

# In summary, hashable objects have a constant hash value and can be used as keys in dictionaries and elements in sets, while unhashable objects do not have a constant hash value and cannot be used in these contexts.


'''
Not exactly. The concept of hashable and unhashable objects in Python is more about the ability to compute a consistent hash value for an object, which is used for quick lookups in data structures like dictionaries and sets.

### Hashable Objects
- **Definition**: An object is hashable if it has a hash value that does not change during its lifetime. This allows the object to be used as a key in a dictionary or as an element in a set.
- **Characteristics**:
  - **Immutable**: Hashable objects are typically immutable, meaning their state cannot be changed after they are created.
  - **Consistent Hash Value**: The hash value of the object remains constant.
  - **Examples**: `int`, `float`, `str`, `tuple` (if all elements are hashable), 

frozenset

.

### Unhashable Objects
- **Definition**: An object is unhashable if it does not have a consistent hash value. This means it cannot be used as a key in a dictionary or as an element in a set.
- **Characteristics**:
  - **Mutable**: Unhashable objects are typically mutable, meaning their state can be changed after they are created.
  - **No Consistent Hash Value**: The hash value of the object can change if the object's state changes.
  - **Examples**: `list`, `dict`, `set`.



### Summary
- **Hashable Objects**: Have a consistent hash value and can be used as keys in dictionaries and elements in sets. They are typically immutable.
- **Unhashable Objects**: Do not have a consistent hash value and cannot be used as keys in dictionaries or elements in sets. They are typically mutable.

The distinction is not about pointing directly to something or being a reference to something, but rather about the ability to compute a consistent hash value for the object.


'''