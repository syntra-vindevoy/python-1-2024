# nederlandstalige functies gezien de opgave

def opp_driehoek(h, b):
    return 0.5 * h * b

def opp_rechthoek(h, b):
    return h * b


def parabool_y(x):
    return x**2

def opp_segment(x1, x2):
    # bewust afgeweken met benaming voor duidelijkheid
    # functie is eigenlijk overbodig, en zou in opp_gesegmenteerd kunnen opgenomen worden
    # ik behoud dit liever voor de duidelijkheid, liever een extra stap
    basis = x2 - x1
    hoogte1 = parabool_y(x1)
    hoogte2 = parabool_y(x2)

    return opp_rechthoek(basis, hoogte1)+ opp_driehoek(hoogte2 - hoogte1, basis)

def opp_gesegmenteerd(x1, x2, n=1):
    #bewust met benaming afgeweken ifv duidelijkheid
    basis = (x2 - x1) / n
    return sum(opp_segment(x1 + i * basis, x1 + (i + 1) * basis) for i in range(n))

def opp_parabool(x1, x2):
    # bewust voor 5 digits gekozen ipv 4 om afrondingsfouten te voorkomen
    n = 1
    vorig_resultaat = opp_gesegmenteerd(x1, x2, n)
    while True:
        n *= 2
        nieuw_resultaat = opp_gesegmenteerd(x1, x2, n)
        if round(nieuw_resultaat, 5) == round(vorig_resultaat, 5):
            return round(nieuw_resultaat, 4) # 4 digits ivm opgave
        vorig_resultaat = nieuw_resultaat

def main():
    print(opp_parabool(0, 4))

if __name__ == "__main__":
    main()

