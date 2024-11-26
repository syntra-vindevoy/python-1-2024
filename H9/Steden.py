Steden = ["Oudenaarde", "Erpe-mere", "Deinze", "Zottegem", "Wetteren", "Gent", "Aalst", "Ninove", "Aalter", "Opwijk", "Mariakerke"]

for stad in Steden[:]:
    if stad[0].lower() in "aeiou":
        Steden.remove(stad)

print(Steden)
