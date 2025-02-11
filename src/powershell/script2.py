import json
import sys


def verwerk_lijst(lijst):
    """Converteert een lijst van woorden naar een dictionary met extra informatie."""
    return {
        woord: {
            "lengte": len(woord),
            "omgekeerd": woord[::-1]
        }
        for woord in lijst
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gebruik: python script.py <woord1> <woord2> ...")
        sys.exit(1)

    # Verkrijg de lijst uit de argumenten
    lijst = sys.argv[1:]  # Strings blijven strings
    resultaat = verwerk_lijst(lijst)

    # Print JSON, zodat PowerShell het kan verwerken
    print(json.dumps(resultaat))
