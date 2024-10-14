# https://colab.research.google.com/github/AllenDowney/ThinkPython/blob/v3/chapters/chap02.ipynb#scrollTo=f92afde0

# Chap02.ipynb

# Repeating my advice from the previous chapter, whenever you learn a new feature,
# you should make errors on purpose to see what goes wrong.


print("-----------------------------------------------------")
print("Part1 : ")
# Define the radius of the sphere in centimeters
radius = 5  # radius in centimeters

# Calculate the volume of the sphere using the formula
volume = (4/3) * 3.14159 * (radius ** 3)  # volume in cubic centimeters

# Display the result
print("The volume of the sphere is:", volume, "cubic centimeters")


print("-----------------------------------------------------")
print("Part2 : ")
# A rule of trigonometry says that for any value of  𝑥 ,  (cos𝑥)2+(sin𝑥)2=1 .
# Let's see if it's true for a specific value of  𝑥  like 42.
# Create a variable named x with this value. Then use math.cos and math.sin
# to compute the sine and cosine of  𝑥 , and the sum of their squared.
# The result should be close to 1.
# It might not be exactly 1 because floating-point arithmetic is not exact---it is only approximately correct.

import math

# Assign the value to variable x
x = 42

# Compute the sine and cosine of x
sin_x = math.sin(math.radians(x))  # Convert degrees to radians
cos_x = math.cos(math.radians(x))  # Convert degrees to radians

# Compute the sum of their squares
result = (cos_x)**2 + (sin_x)**2

# Print the result
print("Result:", result)


print("-----------------------------------------------------")
print("Part3 : ")
# In addition to pi, the other variable defined in the math module is e,
# which represents the base of the natural logarithm, written in math notation as  𝑒 .
# If you are not familiar with this value, ask a virtual assistant "What is math.e?"
# Now let's compute  𝑒2  three ways:

import math

# Method 1: Using math.e and the exponentiation operator (**)
result1 = math.e ** 2

# Method 2: Using math.pow
result2 = math.pow(math.e, 2)

# Method 3: Using math.exp
result3 = math.exp(2)

print("Using math.e and the exponentiation operator:", result1)
print("Using math.pow:", result2)
print("Using math.exp:", result3)




# 1. We've seen that n = 17 is legal. What about 17 = n?
# Because the correct syntax for assignment is to place the variable name
# on the left side of de the = operator. "n = 17"


# 2. How about x = y = 1?
# is legal in Python. This statement assigns the value 1 to
# both variables y and x simultaneously. It is a valid chain assignment,
# where y gets 1, and then x gets the value of y (which is also 1).

# 3. What happens if you put a semi-colon at the end of a Python statement?
# In Python, the use of a semi-colon (;) at the end of a statement
# is optional and does not affect the execution of the code. It is ignored,
# so print("Hello World"); is equivalent to print("Hello World").

# 4. What if you put a period at the end of a statement?
# Using a period at the end of a statement in Python will typically result
# in a syntax error. For example, print("Hello World"). would be invalid in Python.
# The period isn't expected in general statement syntax and can lead to confusion.

# 5. What happens if you spell the name of a module wrong and try to import maath?
# If you try to import a non-existent module, such as maath, using the statement
# import maath, Python will raise an ImportError (or ModuleNotFoundError in more
# recent versions of Python), stating that the module does not exist. For example,
# you'll get an error message similar to ModuleNotFoundError: No module named 'maath'.



# The volume of a sphere with radius  𝑟  is  43𝜋𝑟3 . What is the volume of a sphere
# with radius 5? Start with a variable named radius and then assign the result to a
# variable named volume. Display the result. Add comments to indicate that radius is
# in centimeters and volume in cubic centimeters.