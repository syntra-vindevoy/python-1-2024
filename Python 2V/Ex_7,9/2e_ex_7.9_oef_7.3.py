import math

def estimate_pi():
    sum = 0
    epsilon = 1e-15  # Kleinere en leesbare notatie voor epsilon
    k = 0

    while True:
        i = (math.factorial(4 * k) * (1103 + 26390 * k)) / (math.pow(math.factorial(k), 4) * math.pow(396, 4 * k))
        if i < epsilon:
            break
        sum += i
        k += 1

    inverse = 2 * math.sqrt(2) * sum / 9801
    return 1 / inverse

def test_square_root():
    """
    Test de estimate_pi functie en vergelijk het resultaat met de ingebouwde math.pi waarde.
    """
    print(f"Geschatte Pi: {estimate_pi()}")
    print(f"Math Pi: {math.pi}")
    print(f"Verschil: {estimate_pi() - math.pi}")

# Test de estimate_pi functie
print(f"De wortel van 4 is ongeveer: {estimate_pi():.5f}")

# Voer de test uit
test_square_root()
