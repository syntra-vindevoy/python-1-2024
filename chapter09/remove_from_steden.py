steden = ["oudenaarde", "Zottegem", "Sint-niklaas", "Kortrijk",
          "Deinze", "Gent", "Lede", "Erpe-Mere", "Wetteren", "Aalst", "Aalter", "Ninove", "Opwijk"]
klinkers = ["a","e","i","o","u","y"]

#dit is een manier
#for stad in steden[:]:
#   if stad[0].lower() in klinkers:
# steden.remove(stad)

#betere manier om dit op te lossen is om de lijst van vanachter beginnen te controleren.
#zef geschreven tijdens het voorbeeld van de for i in length...
for stad in steden[::-1]:
    if stad[0].lower() in klinkers:
        steden.remove(stad)

print(steden)
