def add_one(num):
    if(num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)

mynewtotal = add_one(0)
print(mynewtotal)

value = True
while value:#while value is true
    print(value)
    value = False #or 0

value = "y"
count = 0
while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0
        continue