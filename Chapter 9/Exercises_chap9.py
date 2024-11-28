#maak een lijst met steden en smijt uit de lijst alle steden die beginnen met een klinker
steden = ["Oudenaarde", "Zottegem", "Sint-Niklaas", "Kortrijk", "Deinze", "Gent", "Lede", "Erpe-Mere", "Wetteren", "Aalst", "Ninove", "Aalter", "Opwijk", ]
vowels = ["a", "e", "i", "o", "u", "y"]

for stad in steden[::-1]:
    print("Ik controleer ", stad)
    begin = stad[0].lower()

    if begin in vowels:
        print("Ik verwijder ", stad)
        steden.remove(stad)

print(f"De overgebleven steden zijn {steden}")

#ChatGPT oplossing:
#steden = [stad for stad in steden if stad[0].lower() not in vowels]
