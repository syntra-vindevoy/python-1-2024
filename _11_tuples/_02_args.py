# Define a function 'mean' that accepts a variable number of arguments (*args)
# '*args' allows you to pass a variable number of positional arguments to the function
def mean(*args):
    return sum(args) / len(args)  # Calculate and return the mean of all arguments

print(mean(1, 2, 3, 4, 5))

# Define a list of numbers
t = [1, 2, 3, 4, 5]
print(mean(*t))  # Use unpacking (*) to pass the list elements as arguments to the 'mean' function


# Define another function 'test' that accepts keyword arguments (**kwargs)
# '**kwargs' allows passing a variable number of keyword arguments to the function
def ttest(**kwargs):
    # Iterate through the keyword arguments and print their key and value pairs
    for kw in kwargs:
        print(f"{kw}: {kwargs[kw]}")  # Use f-string to format and display key-value pairs


print(ttest(a=1, b=2, c=3))  # Call the function with keyword arguments and print the output

# Define a dictionary
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(ttest(**d))  # Use unpacking (**) to pass the dictionary as keyword arguments to the 'test' function


# Define a function 'homepage' that accepts an obligatory 'request' parameter,
# along with optional positional arguments (*args) and keyword arguments (**kwargs).
# This structure is commonly used in web frameworks like Django to handle HTTP requests.
def homepage(request, *args, **kwargs):
    pass