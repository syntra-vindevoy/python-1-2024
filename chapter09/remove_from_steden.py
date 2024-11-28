steden = ["oudenaarde", "Zottegem", "Sint-niklaas", "Kortrijk",
          "Deinze", "Gent", "Lede", "Erpe-Mere", "Wetteren", "Aalst", "Aalter", "Ninove", "Opwijk"]
klinkers = ["a","e","i","o","u","y"]

for stad in steden[:]:
    if stad[0].lower() in klinkers:
        steden.remove(stad)

print(steden)
