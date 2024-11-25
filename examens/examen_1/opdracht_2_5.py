"""
opdracht 2.5
author : Benoit Goethals
"""


def opp_driehoek(h: float, b: float) -> float:
    """
    Bereken de oppervlakte van een driehoek.

    :param h: De hoogte van de driehoek.
    :param b: De basis van de driehoek.
    :return: De oppervlakte van de driehoek.
    """
    return (h * b) / 2


assert opp_driehoek(1, 1) == 0.5, "Test case hoogte=1, basis=1 mislukt"
assert opp_driehoek(2, 2) == 2.0, "Test case hoogte=2, basis=2 mislukt"
assert opp_driehoek(3, 3) == 4.5, "Test case hoogte=3, basis=3 mislukt"


def opp_vierkant(h: float, b: float) -> float:
    """
    Bereken de oppervlakte van een vierkant/rechthoek.

    :param h: De hoogte van het vierkant/rechthoek.
    :param b: De basis van het vierkant/rechthoek.
    :return: De oppervlakte van het vierkant/rechthoek.
    """
    return h * b


assert opp_vierkant(1, 1) == 1, "Test case hoogte=1, basis=1 mislukt"
assert opp_vierkant(2, 2) == 4, "Test case hoogte=2, basis=2 mislukt"
assert opp_vierkant(3, 3) == 9, "Test case hoogte=3, basis=3 mislukt"


def opp(x1: float, x2: float, y1: float, y2: float) -> float:
    """
    :param x1: The x-coordinate of the first point.
    :param x2: The x-coordinate of the second point.
    :param y1: The y-coordinate of the first point.
    :param y2: The y-coordinate of the second point.
    :return: The combined area of the rectangle and the triangle formed by the given points.
    """
    # Oppervlakte rechthoek
    oppervlakte_rechthoek = opp_vierkant(x2 - x1, y1)
    # Oppervlakte driehoek
    oppervlakte_driehoek = opp_driehoek(x2 - x1, y2 - y1)

    return oppervlakte_driehoek + oppervlakte_rechthoek


assert opp(0, 3, 0, 2) == 3


def parabool(x: float) -> float:
    """
    Simple parabool function
    :param x: A float input value
    :return: The square of the input value as a float
    """
    return x ** 2


def approximate_area_with_line(x1, x2):
    """
    :param x1: The first x-coordinate forming the base of the trapezoid
    :param x2: The second x-coordinate forming the base of the trapezoid
    :return: The approximate area under the curve between x1 and x2 using the trapezoidal rule
    """
    y1 = parabool(x1)
    y2 = parabool(x2)
    return (y1 + y2) * (x2 - x1) / 2


def approximate_area_with_intermediate_point(x1, x2):
    """
    The approximate_area_with_intermediate_point function uses the intermediate midpoint to split the interval [x1, x2]
    into two smaller intervals. It then approximates the area under the curve for each smaller interval using
    the approximate_area_with_line function and sums these areas to get the total approximate area under
    the curve between x1 and x2.
    :param x1: The first x-coordinate
    :param x2: The second x-coordinate
    :return: The approximate area under a curve, calculated using intermediate points
    """
    x_mid = (x1 + x2) / 2
    y1 = parabool(x1)
    y2 = parabool(x2)
    y_mid = parabool(x_mid)
    return approximate_area_with_line(x1, x_mid) + approximate_area_with_line(x_mid, x2)


# Calculate the area using both methods
area_with_line = approximate_area_with_line(0, 4)
area_with_intermediate_point = approximate_area_with_intermediate_point(0, 4)

print("Area approximated with a line:", area_with_line)
print("Area approximated with an intermediate point:", area_with_intermediate_point)

"""
opdracht 2.5
Geen imports
"""


def opp_parabool(x1: float, x2: float) -> float:
    """
    Benader de oppervlakte onder de parabool

    :param x1: De x-coördinaat van het beginpunt.
    :param x2: De x-coördinaat van het eindpunt.
    :return: De benaderde oppervlakte onder de parabool van x1 tot x2.
    """
    n = 1000  # Het aantal onderverdelingen voor de benadering.
    totale_oppervlakte = 0
    dx = (x2 - x1) / n
    for i in range(n):
        x_start = x1 + i * dx
        x_eind = x_start + dx
        rechthoek_hoogte = x_start ** 2
        rechthoek_oppervlakte = opp_vierkant(rechthoek_hoogte, dx)
        driehoek_basis = dx
        driehoek_hoogte = (x_eind ** 2) - rechthoek_hoogte
        driehoek_oppervlakte = opp_driehoek(driehoek_hoogte, driehoek_basis)
        totale_oppervlakte += rechthoek_oppervlakte + driehoek_oppervlakte
    return totale_oppervlakte


oppervlakte = opp_parabool(0, 4)
verwachte_oppervlakte = 64 / 3
assert abs(oppervlakte - verwachte_oppervlakte) < 0.01, f"Test case x1=0, x2=4 mislukt: {oppervlakte}"
