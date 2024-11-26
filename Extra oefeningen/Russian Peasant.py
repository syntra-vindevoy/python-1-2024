def russian_peasant(a: int, b: int) -> int:
    if b == 0:
        return 0
    #Remove every row in the halving column that has an even answer
    elif b % 2 != 0:
    #Now take the sum of all the answers in the doubling column for your answer!
        return a + russian_peasant(a * 2, b // 2)
    #repeat until b/2 = 0 (0.5 == 0)
    else:
        return russian_peasant(a * 2, b // 2)

print(russian_peasant(543, 977))

