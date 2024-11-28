def higher_lower(min:int, max:int, n:int) -> int:
    i = 0

    while True:
        ranges = [min, max]
        i += 1
        limit = sum(ranges) // 2

        if n == limit:
            print("found")
            return i
        elif n < limit:
            #print("lower")
            max = limit - 1
        elif n > limit:
            #print("higher")
            min = limit + 1

print(higher_lower(1, 10000, 3112))
print(higher_lower(1, 10000, 0))
print(higher_lower(1, 10000, 10000))

print(higher_lower(1, 1000000, 500000))

