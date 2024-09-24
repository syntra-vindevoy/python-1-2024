#integer
print(type(765))
#float
print(type(2.718))
#string
print(type('2 pi'))
#integer
print(type(abs(-7)))
#float
print(type(abs(-7.0)))
#function
print(type(abs))
#type
print(type(int))
#type
print(type(int))
#type
print(type(type))

print(240 // 60)
print((60 * 42 + 42), "seconds")
print((10 / 1.61), "miles")
print(round(((60 * 42 + 42) / (10 / 1.61))), "s/mile")

minutes = int(((60 * 42 + 42) / (10/1.61)) // 60)
seconds = round((60 * 42 + 42) / (10 / 1.61) % 60)
print(f"{minutes} minutes and {seconds} seconds per mile")

print(3600 / ((minutes * 60 ) + seconds))
