def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(isprime(27))

#1) is het deelbaar door 2? 1 x checken alvorens je aan je lus begint dus het eerste deel kan meer performant gemaakt worden
#2) range moet gaan tot square root + 1
