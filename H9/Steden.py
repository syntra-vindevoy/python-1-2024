Steden = ["Oudenaarde", "Erpe-mere", "Deinze", "Zottegem", "Wetteren", "Gent", "Aalst", "Ninove", "Aalter", "Opwijk", "Mariakerke"]

for name in Steden[:]:
    if name[0].lower() in "aeiou":
        Steden.remove(name)

print(Steden)
