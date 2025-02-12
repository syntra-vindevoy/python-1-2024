class Parachutist:
    def __init__(self, lichaamsgewicht, aflaatbaar=False, gewicht_aflaatbaar=0):
        self.lichaamsgewicht = lichaamsgewicht
        self.aflaatbaar = aflaatbaar
        self.gewicht_aflaatbaar = gewicht_aflaatbaar

    def drop_material(self):
        """Laat aflaatbaar materiaal vallen, zodat het gewicht niet meer meetelt."""
        self.aflaatbaar = False
        self.gewicht_aflaatbaar = 0

    def __call__(self, aantal):
        """Bereken het totale gewicht van alle parachutisten, inclusief of exclusief materiaal."""
        totaal_gewicht = aantal * (self.lichaamsgewicht + (self.gewicht_aflaatbaar if self.aflaatbaar else 0))
        return totaal_gewicht


class ParachutistGroep:
    def __init__(self, parachutisten):
        """Initialiseer met een lijst van parachutisten en hun gewichten."""
        self.parachutisten = parachutisten  # Lijst met (naam, gewicht)-tuples

    # Representatie
    def __str__(self):
        return f"Parachutistengroep met {len(self.parachutisten)} parachutisten."

    def __repr__(self):
        return f"ParachutistGroep({self.parachutisten})"

    # Vergelijkingen (op basis van totaal gewicht)
    def totaal_gewicht(self):
        return sum(gewicht for _, gewicht in self.parachutisten)

    def __eq__(self, other):
        return self.totaal_gewicht() == other.totaal_gewicht()

    def __lt__(self, other):
        return self.totaal_gewicht() < other.totaal_gewicht()

    def __le__(self, other):
        return self.totaal_gewicht() <= other.totaal_gewicht()

    def __gt__(self, other):
        return self.totaal_gewicht() > other.totaal_gewicht()

    def __ge__(self, other):
        return self.totaal_gewicht() >= other.totaal_gewicht()

    # Wiskundige operaties (schaalt gewicht van alle parachutisten)
    def __add__(self, extra_gewicht):
        return ParachutistGroep([(naam, gewicht + extra_gewicht) for naam, gewicht in self.parachutisten])

    def __sub__(self, minder_gewicht):
        return ParachutistGroep([(naam, max(0, gewicht - minder_gewicht)) for naam, gewicht in self.parachutisten])

    def __mul__(self, factor):
        return ParachutistGroep([(naam, gewicht * factor) for naam, gewicht in self.parachutisten])

    def __truediv__(self, factor):
        return ParachutistGroep([(naam, gewicht / factor) for naam, gewicht in self.parachutisten])

    # Callable: bereken totaalgewicht voor een bepaald aantal groepen
    def __call__(self, aantal_groepen):
        return self.totaal_gewicht() * aantal_groepen

    # Itereren over parachutisten
    def __iter__(self):
        return iter(self.parachutisten)

    # Container methodes
    def __getitem__(self, index):
        return self.parachutisten[index]

    def __setitem__(self, index, value):
        self.parachutisten[index] = value

    def __delitem__(self, index):
        del self.parachutisten[index]

    def __contains__(self, naam):
        return any(parachutist[0] == naam for parachutist in self.parachutisten)

    def __len__(self):
        return len(self.parachutisten)

    # += Toevoegen van extra gewicht aan alle parachutisten
    def __iadd__(self, extra_gewicht):
        self.parachutisten = [(naam, gewicht + extra_gewicht) for naam, gewicht in self.parachutisten]
        return self

    # -= Gewicht verminderen voor alle parachutisten
    def __isub__(self, minder_gewicht):
        self.parachutisten = [(naam, max(0, gewicht - minder_gewicht)) for naam, gewicht in self.parachutisten]
        return self

    # *= Gewicht vermenigvuldigen (bijv. om een zware uitrusting te simuleren)
    def __imul__(self, factor):
        self.parachutisten = [(naam, gewicht * factor) for naam, gewicht in self.parachutisten]
        return self

    # /= Gewicht delen door een factor
    def __itruediv__(self, factor):
        self.parachutisten = [(naam, gewicht / factor) for naam, gewicht in self.parachutisten]
        return self

    # //= Gehele deling van gewicht
    def __ifloordiv__(self, factor):
        self.parachutisten = [(naam, gewicht // factor) for naam, gewicht in self.parachutisten]
        return self

    # %= Modulo-bewerking op gewicht
    def __imod__(self, waarde):
        self.parachutisten = [(naam, gewicht % waarde) for naam, gewicht in self.parachutisten]
        return self


if __name__ == "__main__":

    # Voorbeeldgebruik
    parachutist1 = Parachutist(80, aflaatbaar=True, gewicht_aflaatbaar=20)  # 80kg + 20kg materiaal

    # Bereken gewicht vóór materiaal wordt gedropt
    totaal_voor = parachutist1(5)  # 5 parachutisten mét aflaatbaar materiaal
    print(f"Totale gewicht vóór droppen: {totaal_voor} kg.")

    # Droppen van materiaal
    parachutist1.drop_material()

    # Bereken gewicht ná materiaal is gedropt
    totaal_na = parachutist1(5)  # 5 parachutisten zonder extra materiaal
    print(f"Totale gewicht ná droppen: {totaal_na} kg.")

    # --- Gebruik ---
    groep1 = ParachutistGroep([("Jan", 80), ("Lisa", 70), ("Mark", 90)])
    groep2 = ParachutistGroep([("Anna", 85), ("Tom", 75)])

    # Representatie
    print(str(groep1))  # "Parachutistengroep met 3 parachutisten."
    print(repr(groep1))

    # Vergelijkingen
    print(groep1 > groep2)  # True of False

    # Wiskundige operaties
    groep_zwaarder = groep1 + 5
    groep_lichter = groep1 - 5
    groep_dubbel = groep1 * 2

    print(groep_zwaarder.totaal_gewicht())  # Iedereen +5 kg
    print(groep_lichter.totaal_gewicht())  # Iedereen -5 kg

    # Callable: Bereken totaalgewicht voor 3 groepen
    print(groep1(3))  # 3 keer het totale gewicht

    # Itereren
    for parachutist in groep1:
        print(parachutist)  # ("Jan", 80), ("Lisa", 70), ...

    # Containers
    print(groep1[1])  # ("Lisa", 70)
    groep1[1] = ("Lisa", 75)  # Gewicht aanpassen
    del groep1[0]  # Jan verwijderen
    print("Mark" in groep1)  # True of False

    # Lengte van de groep
    print(len(groep1))  # Aantal parachutisten

    # --- Gebruik ---
    groep = ParachutistGroep([("Jan", 80), ("Lisa", 70), ("Mark", 90)])

    print(groep)  # "Parachutistengroep met totaal 240 kg."

    groep += 5  # Iedereen +5 kg
    print(groep)  # 255 kg

    groep -= 10  # Iedereen -10 kg
    print(groep)  # 225 kg

    groep *= 2  # Gewicht verdubbelen
    print(groep)  # 450 kg

    groep /= 3  # Gewicht door 3 delen
    print(groep)  # 150 kg

    groep //= 2  # Gehele deling
    print(groep)  # 75 kg

    groep %= 30  # Modulo 30 (gewicht wordt rest bij delen door 30)
    print(groep)  # 15 kg

    C = [39.2, 36.5, 37.3, 38, 37.8]
    F = list(map(lambda x: (float(9) / 5) * x + 32, C))
    print(F)

    from math import sin, cos, tan, pi


    def map_functions(x, functions):
        """ map an iterable of functions on the the object x """
        res = []
        for func in functions:
            res.append(func(x))
        return res


    family_of_functions = (sin, cos, tan)
    print(map_functions(pi, family_of_functions))

    C = [39.2, 36.5, 37.3, 38, 37.8]
    F = [(9 / 5) * x + 32 for x in C]
    print(F)


    def map_functions(x, functions):
        """ Map an iterable of functions on the object x using list comprehension """
        return [func(x) for func in functions]


    family_of_functions = (sin, cos, tan)
    print(map_functions(pi, family_of_functions))
