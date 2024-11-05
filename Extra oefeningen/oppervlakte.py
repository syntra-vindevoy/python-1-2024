#oppervlakte van driehoek en vierhoek

def oppervlakte_driehoek(basis, hoogte):
    return (basis * hoogte) / 2

basis = int(input("Wat is de basis van de driehoek? "))
hoogte = int(input("Wat is de hoogte van de driehoek? "))
oppervlakte = oppervlakte_driehoek(basis, hoogte)

print(f"De oppervlakte van de driehoek is {oppervlakte}")


def oppervlakte_vierkant(basis, hoogte):
    return (basis * hoogte)

basis = int(input("Wat is de basis van de vierkant? "))
hoogte = int(input("Wat is de hoogte van de vierkant? "))
oppervlakte = oppervlakte_vierkant(basis, hoogte)

print(f"De oppervlakte van de vierkant is {oppervlakte}")