
# https://www.youtube.com/watch?v=7xAJVNUEZS0


test_list = [1, 2, 3, 4, 5]

def square(x):
    return x * x

result = map(square, test_list)
print(list(result))  # [1, 4, 9, 16, 25]

# The map function takes a function and an iterable as arguments and applies the function to each element of the iterable.

# The map function returns a map object, which is an iterator. To get the result as a list, you can convert the map object to a list using the list function.

# calculations are done in the print-line in this example...!!!

some_function = lambda x: x * x
print(list(map(some_function, test_list)))  # [1, 4, 9, 16, 25]
