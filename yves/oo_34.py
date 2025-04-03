customers = [
    {"name": "John", "address": "123 Main St", "age": 30},
    {"name": "Jane", "address": "456 Main St", "age": 25},
    {"name": "John", "address": "789 Main St", "age": 20}
]


def my_lambda(x):
    return x["name"], x["age"]

customers.sort(key=lambda x: (x["name"], x["age"]))

print(customers)


lst = [1,2, 3]

print(list(map(lambda x: x * 2, lst)))

