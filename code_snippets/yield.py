def tel_tot(n):
    for i in range(n):
        yield i


# Gebruik van de generator
for nummer in tel_tot(5):
    print(nummer)
