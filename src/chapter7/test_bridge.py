from itertools import combinations
"""
Uitleg van het Algoritme
We sorteren de groep op snelheid, van snel naar langzaam.
Zolang er meer dan drie personen zijn, worden er telkens twee mensen naar de overkant gebracht op 
een manier die de totale tijd minimaliseert. Er zijn hiervoor twee strategieën:
Stuur de twee snelste naar de overkant, en laat de snelste terugkomen.
Stuur de snelste en traagste naar de overkant, en laat de snelste terugkomen.
Voor de laatste drie personen wordt de resterende tijd berekend door de oversteek met de traagste
 van de laatste drie te voltooien.
"""

# Functie om de tijd van een oversteek te berekenen
def cross_time(person1, person2):
    return max(person1, person2)


# Functie om de totale oversteektijd te berekenen
def calculate_min_time(people):
    # Sorteer mensen op snelheid, van snelst naar traagst
    people.sort()
    total_time = 0

    while len(people) > 3:
        # Optimaliseer voor de snelste en traagste persoon
        # Methode 1: De snelste twee gaan en snelste keert terug
        option1 = 2 * people[1] + people[0] + people[-1]
        # Methode 2: Snelste en traagste gaan eerst, snelste keert terug
        option2 = 2 * people[0] + people[-1] + people[-2]

        total_time += min(option1, option2)
        people = people[:-2]  # Haal de twee traagste eruit (ze zijn overgestoken)

    # Bij de laatste drie personen
    if len(people) == 3:
        total_time += people[0] + people[1] + people[2]
    elif len(people) == 2:
        total_time += cross_time(people[0], people[1])
    elif len(people) == 1:
        total_time += people[0]

    return total_time

if __name__ == '__main__':
    # Voorbeeld: Vier mensen met verschillende tijden
    people = [1, 2, 5, 10]  # Minuten die ze nodig hebben om de brug over te steken
    min_time = calculate_min_time(people)

    print(f"Minimale tijd om iedereen over te steken: {min_time} minuten")