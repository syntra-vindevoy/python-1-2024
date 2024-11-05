def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1  # Startwaarden voor de Fibonacci-reeks

    for _ in range(n):
        fib_sequence.append(a)  # Voeg de huidige waarde toe aan de reeks
        a, b = b, a + b  # Update a en b naar de volgende Fibonacci-getallen

    return fib_sequence

# Voorbeeld van het gebruik
n = 10  # Aantal Fibonacci-getallen dat je wilt genereren
result = fibonacci(n)
print(result)
