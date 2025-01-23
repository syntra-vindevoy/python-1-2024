def dict_words():
    with open ("words.txt", "r") as f:
        words_dict = { word: 1 for word in f.read().splitlines()}

        return words_dict
#print (dict_words())

def is_in(word):
    return word in dict_words()

#print (is_in("chocolate"))

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "green",
}
#car ["color"] = "white"
car.setdefault("color", "white")
#setdefault vult de dict aan als de key nog niet bestaat, als deze bestaat, veranderd de value niet

print(car)

def invert_dict(dict_to_invert):
    new_dict = {}
    for key, value in dict_to_invert.items():
        new_dict.setdefault(value,key)

    return new_dict
x = {"a":1 , "b":2, "c":3 }
print(invert_dict(x))




