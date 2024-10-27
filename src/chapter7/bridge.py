"""
Bij het bekende probleem van het "bridge passing" of "brug-oversteek"-algoritme moeten een aantal mensen 's nachts over een brug oversteken met een enkele zaklamp en een beperkte tijd. Het doel is dat iedereen veilig over de brug komt binnen de gegeven tijd, ondanks de beperkingen in snelheid en zaklampgebruik.

Probleemstelling
Er zijn N personen die over een brug moeten oversteken.
Elke persoon heeft een andere snelheid om de brug over te steken (uitgedrukt in minuten).
Slechts 2 personen kunnen tegelijk oversteken, omdat de brug te smal is.
Een zaklamp is nodig om over te steken, en er is maar één zaklamp.
Telkens wanneer 2 personen oversteken, moet iemand de zaklamp terugbrengen.

Doel
Iedereen moet binnen de toegestane tijd aan de overkant zijn, met zo min mogelijk tijdsverspilling.

Voorbeeld
Stel, we hebben 4 personen met de volgende tijden om de brug over te steken:

Persoon A: 1 minuut
Persoon B: 2 minuten
Persoon C: 5 minuten
Persoon D: 10 minuten
Het doel is om alle vier aan de overkant te krijgen met een minimaal aantal minuten.

Algoritme Oplossing
Sorteren van tijden: Sorteer de personen op basis van hun oversteektijden.
Optimaliseren van oversteken:
Er zijn doorgaans twee strategieën om de totale tijd te minimaliseren:
Langzaamste eerst overbrengen: Laat steeds de twee langzaamste overgaan en de snelste terugkomen.

1. Sorteer de personen op basis van hun oversteektijd in oplopende volgorde.
2. Terwijl er meer dan twee mensen zijn aan de kant van de brug:
     a. Laat de snelste en tweede snelste oversteken en noteer de tijd.
     b. Laat de snelste teruggaan en noteer de tijd.
     c. Laat de langzaamste en op één-na-langzaamste oversteken en noteer de tijd.
     d. Laat de tweede snelste teruggaan en noteer de tijd.
3. Wanneer er twee mensen over zijn, laat hen samen oversteken.
4. Som de totale tijd op.

Voorbeeld Resultaat
Laten we dit pseudocode uitvoeren op ons voorbeeld:

Eerst steken A en B over (1 + 2 = 3 minuten).
A keert terug (1 minuut).
C en D steken over (10 minuten).
B keert terug (2 minuten).
A en B steken samen over (2 minuten).
Totale tijd = 3 + 1 + 10 + 2 + 2 = 18 minuten.

"""

TIME_PERSONS = {
    "A": 1,
    "B": 2,
    "C": 5,
    "D": 10,}

def convert_to_dict(side):
    my_dict = {}
    for person in side:
        my_dict[person] = (TIME_PERSONS[person])
    return my_dict.items()

def get_fastest(side:[],count)->[]:
    return [item[0] for item in sorted(convert_to_dict(side), key=lambda item: item[1])[:count]]

def get_slowest(side:[],count)->[]:
    return [item[0] for item in sorted(convert_to_dict(side), reverse=True, key=lambda item: item[1])[:count]]

def move_too(pers_to_move:[], from_side:[], too_side:[]):
    for person in pers_to_move:
        from_side.remove(person)
        too_side.append(person)



def main():
    right_side= []
    left_side = list(TIME_PERSONS.keys())
    total_time = 0
    side=0

    while len(left_side) > 0:
        if side == 1:
            fastest = get_fastest(right_side,1)
            move_too(fastest, right_side, left_side)
        else:
            fastest = get_slowest(left_side,2)
            move_too(fastest, left_side, right_side)
        side = not side
        for person in fastest:
            total_time += TIME_PERSONS[person]
        print(left_side,right_side)
    print(total_time)

if __name__ == '__main__':
    main()