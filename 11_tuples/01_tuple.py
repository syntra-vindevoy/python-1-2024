# Defining a tuple using parentheses
x = (1, 2)

# Defining a tuple without parentheses (parentheses are optional)
y = 1, 2

# Printing the type of x to confirm it is a tuple
print(type(x))

# Printing the type of y to confirm it is a tuple as well
print(type(y))


a = 1  # Assign 1 to variable 'a'
b = 2  # Assign 2 to variable 'b'

# Swap the values of 'a' and 'b'
a, b = (b, a)

c = (a, b)


# Create a tuple from the string "Thomas" (Each character becomes an element of the tuple)
y = tuple("Thomas")
print(y)
print(y[0])
print(len(y))
print(sorted(y))

# Create a tuple with a single element ("Thomas") by including a trailing comma
x = ("Thomas",)
print(x)
print(x[0])
print(len(x))

# Create a tuple with mixed data types (including a list as one of the elements)
t = (1, 2, "a", [1, 2, 3])
# print(sorted(t))  # This line is commented out because it would raise an error.
# Sorting a tuple with mixed data types is not allowed in Python.


# Assign values 1 and 2 to variables 'a' and 'b' respectively, and ignore the third value (3) using '_'
a, b, _ = 1, 2, 3
print(a)
print(b)
print(_)


# Assign values 1 and 2 to variables 'a' and 'b' respectively
# The underscores ('_') are used to ignore the values 3 and 4
# However, the last underscore will retain the value of the final ignored element (4)
a, b, _, _ = 1, 2, 3, 4
print(a)
print(b)
print(_)