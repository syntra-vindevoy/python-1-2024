import math

def mysqrt(a, epsilon=0.00001):
    """
    Bereken de vierkantswortel van 'a' met Newton-Raphson methode.

    Parameters:
        a (float): Het getal waarvan de vierkantswortel wordt berekend.
        epsilon (float): De precisie van de benadering.

    Returns:
        float: De geschatte vierkantswortel van 'a'.
    """
    x = a / 2.0  # Begin met a/2 voor snellere convergentie
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:  # Stop als de benadering nauwkeurig genoeg is
            return y
        x = y

def test_square_root():
    """
    Test de mysqrt functie en vergelijk het resultaat met de ingebouwde math.sqrt functie.
    """
    print("a\tmysqrt(a)\tmath.sqrt(a)\tdiff")
    print("-\t---------\t------------\t----")
    for a in range(1, 10):
        approx = mysqrt(a)  # Bereken mysqrt slechts één keer per waarde
        exact = math.sqrt(a)  # Gebruik math.sqrt om te vergelijken
        diff = approx - exact  # Verschil tussen de benadering en de echte waarde
        print(f"{a}\t{approx:.5f}\t{exact:.5f}\t{diff:.5f}")

# Test de mysqrt functie met een voorbeeld
print(f"De wortel van 4 is ongeveer: {mysqrt(4):.5f}")

# Voer de test voor meerdere waarden van a uit
test_square_root()
