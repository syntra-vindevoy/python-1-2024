def countdown(n):
    for i in range(n, -1, -1):
        print(i if i > 0 else 'Blastoff!')

# Roep de functie aan met 4 als het startgetal voor de countdown
countdown(4)
