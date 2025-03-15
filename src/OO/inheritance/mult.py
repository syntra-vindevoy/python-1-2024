class Transport:
    """Beheert transportmiddelen en hun beschikbaarheid."""

    def verplaats_voertuig(self, voertuig, locatie):
        print(f"{voertuig} wordt verplaatst naar {locatie}.")


class Voorraad:
    """Beheert de voorraad en bevoorradingsniveaus."""

    def controleer_voorraad(self, artikel, hoeveelheid):
        print(f"Controle: {hoeveelheid} eenheden van {artikel} op voorraad.")


class Brandstofbeheer:
    """Berekent brandstofverbruik voor transport."""

    def bereken_brandstof(self, voertuig, afstand):
        verbruik = {"Truck Alpha": 0.3, "Helikopter Bravo": 1.2}  # Liter per km
        if voertuig in verbruik:
            brandstof_nodig = verbruik[voertuig] * afstand
            print(f"{voertuig} verbruikt {brandstof_nodig:.2f} liter brandstof over {afstand} km.")
        else:
            print(f"Geen brandstofgegevens voor {voertuig}.")


class Tijdsbeheer:
    """Berekent de reistijd op basis van afstand en snelheid."""

    def bereken_tijd(self, voertuig, afstand):
        snelheid = {"Truck Alpha": 60, "Helikopter Bravo": 200}  # km/u
        if voertuig in snelheid:
            tijd = afstand / snelheid[voertuig]
            print(f"{voertuig} doet er {tijd:.2f} uur over om {afstand} km af te leggen.")
        else:
            print(f"Geen snelheidsgegevens voor {voertuig}.")


class Herbevoorrading(Transport, Voorraad, Brandstofbeheer, Tijdsbeheer):
    """Combineert transport, voorraadbeheer, brandstof en tijdsbeheer."""

    def plan_bevoorrading(self, artikel, hoeveelheid, voertuig, locatie, afstand):
        print(f"\n=== Bevoorradingsmissie ===")
        print(f"{hoeveelheid}x {artikel} met {voertuig} naar {locatie} ({afstand} km).")
        self.controleer_voorraad(artikel, hoeveelheid)
        self.bereken_brandstof(voertuig, afstand)
        self.bereken_tijd(voertuig, afstand)
        self.verplaats_voertuig(voertuig, locatie)
        print(f"Bevoorrading naar {locatie} voltooid!\n")


# Gebruik van het systeem
missie = Herbevoorrading()
missie.plan_bevoorrading("Munitie", 500, "Truck Alpha", "Logistieke Dump", 150)
missie.plan_bevoorrading("Medische Voorraad", 200, "Helikopter Bravo", "Veldhospitaal", 300)

print(missie.__doc__)
print(missie.__module__)
print(missie.__class__)
print(missie.__dict__)
print(missie.__class__.__bases__)
print(missie.__class__.__mro__)
