costumers = [
    {"name": "John", "age": 30, "is_employed": True},
    {"name": "Anna", "age": 25, "is_employed": False},
    {"name": "Mike", "age": 45, "is_employed": True},
    {"name": "Eva", "age": 18, "is_employed": False},
    {"name": "Alex", "age": 27, "is_employed": True},
]

costumers.sort(key=lambda x: (x["name"], x["age"]))

print(costumers)


list_1 = ["a", "b", "c", "d", "e", "f"]
list_2 = ["d", "f"]

print(list(set(list_1) - set(list_2)))


str = "Tom Van de Vyver"

for char in enumerate(list(str)):
    print(char)

