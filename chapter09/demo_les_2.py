cheeses = ["cheddar","edam","gouda"]

print(cheeses[1]) #we beginnen te tellen van 0, dus 1 is 2de positie

print(cheeses[0:1])
# start bij 0 en gaat tot 2de getal,
# maar 2de getal is er niet meer bij (zoals bij for lus, geeft ook de lijst terug, dus ook [] komen in antwoord.

print(cheeses[0:])
#wanneer we 0: zetten, beginnen we bij 0 en printen we gans de lijst. achter de : geen getal, betekend geen einde

print(cheeses[1::1])
#het 3de getal zorgt ervoor da je gaat springen over bepaalde waardes, hier stijgt het met 1

print(cheeses[1::2])
#hier gaat het met 2 stijgen. start bij positie 1, en gaat naar positie 3. 3 bestaat niet, dus enkel edam wordt getoond

print(cheeses[1::-1]) #begint bij 1, en gaat in omgekeerde volgorde 1 omlaag. dus print pos 1 en pos 0
# - teken zorgt da ge omgekeerd start, dus ge gaat de lijst omgekeerd bekijken

print(cheeses[:1:-1])


print(", ".join(cheeses[:2]))



t1 = [1, 2, 3, 4, 5]
t2 = [4, 5, 6]

#t3 = t1 - t2  dit lukt niet, - teken gaat niet

t3 = set(t1) - set(t2)  #dit lukt wel, retourneerd wel geen lijst terug
print(list(t3))  #als we printen en list rond zetten, dan wordt het wel terug een list.


ip= "192.168.0.80"

print(ip.split(".")) #split zoals in excel, per . wordt hier de string opgedeeld in een lijst


cheeses_sort = ["cheddar", "gouda", "edam"]
sorted(cheeses_sort) # om direct te veranderen, variablele maken, sheeses_sort = sorted(cheeses_sort)

print(cheeses_sort)

cheeses.sort() #dit is een method(classes), dit voert wel effectief direct uit. maar is void functie, retourneert niets