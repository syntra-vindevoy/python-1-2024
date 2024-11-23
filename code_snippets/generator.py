def generate_squares(n):
    for i in range(n):
        yield i**2


for square in generate_squares(10):
    print(square)

# yield: als een berekening eenmaal is gedaan, wordt de waarde opgeslagen en
# wordt de berekening niet opnieuw uitgevoerd
