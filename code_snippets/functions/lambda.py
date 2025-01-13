

def add(x,y):
    return(x+y)
print(add(1,2))

def add(x,y):return(x+y)
print(add(1,2))

add_lambda = lambda x, y: x + y
print(add_lambda(1,2))

print((lambda x,y:x+y)(1,2))



from functools import reduce

add_ten = lambda x: x+10
print(add_ten(5)) # 15

multiply = lambda x,y: x*y
print(multiply(5,5)) # 25

numbers = [1,2,3,4,5]
squared = map(lambda x: x**2, numbers)
print(list(squared)) # [1, 4, 9, 16, 25]


even_numbers = filter(lambda x: x%2==0, numbers)
print(list(even_numbers)) # [2, 4]

points = [(1,2),(3,4),(5,6)]
sorted_points = sorted(points, key=lambda point: point[1])

# lambda with reduce

numbers = [1,2,3,4,5]
product = reduce(lambda x,y: x*y, numbers)

# lambda with default arguments

full_name = lambda first, last="Doe": f"{first} {last}"

print(full_name("John")) # John Doe
print(full_name("John", "Smith")) # John Smith