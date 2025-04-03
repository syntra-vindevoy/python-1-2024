from collections import namedtuple

person = {"name": "John", "age": 36, "city": "New York"}

PersonTuple = namedtuple("PersonTuple", "name age city")
p = PersonTuple(**person)

print(person["name"])
print(p.name)


q = PersonTuple(name="John", age=36, city="New York")
q_person = q._asdict()

print(q_person)

person["age"] = 37
p.age = 38  # error
