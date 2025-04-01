from collections import namedtuple

persons= {
    "name": "John",
    "age": 36,
    "city": "New York"

}

persoon_named_tuple = namedtuple("Person", "name age city")
p = persoon_named_tuple(**persons)
print(p)
q = persoon_named_tuple(name="Jane", age=25, city="Paris")
print(q)

print(p._asdict())