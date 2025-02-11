import json
import sys


def verwerk_lijst(lijst):
    """Zet een lijst om in een dictionary met kwadraten van de getallen."""
    return {str(num): num ** 2 for num in lijst}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gebruik: python script.py <lijst van getallen>")
        sys.exit(1)

    # Verkrijg de lijst uit de argumenten (gescheiden door spaties)
    lijst = list(map(int, sys.argv[1:]))  # Converteer naar integers
    resultaat = verwerk_lijst(lijst)

    # Print JSON, zodat PowerShell het kan verwerken
    print(json.dumps(resultaat))
