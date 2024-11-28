#remove all cities which start with a vowel
steden = ["oudenaarde", "zottegem", "sint-niklaas", "kortrijk", "deinze", "gent", "lede", "erpe-mere", "oostakker", "wetteren", "aalst", "ninove", "aalter", "opwijk"]
cities = ["oudenaarde", "zottegem", "sint-niklaas", "kortrijk", "deinze", "gent", "lede", "erpe-mere", "oostakker", "wetteren", "aalst", "ninove", "aalter", "opwijk"]
dorpen = ["oudenaarde", "zottegem", "sint-niklaas", "kortrijk", "deinze", "gent", "lede", "erpe-mere", "oostakker", "wetteren", "aalst", "ninove", "aalter", "opwijk"]
print(steden)

for stad in steden[::-1]:               #When using a FOR on a list and you remove an element, the elements that come after move index number
    if stad[0] in "aeiouyAEIOUY":
        steden.remove(stad)

print(steden)


print(cities)

for city in cities[::-1]:
    begin = city[0].lower()
    if begin in "aeiouy":
        cities.remove(city)

print(cities)


print(dorpen)
dorpen = [dorp for dorp in dorpen if dorp[0].lower() not in "aeiouy"]
print(dorpen)
