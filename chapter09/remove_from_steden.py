steden = ["oudenaarde", "Zottegem", "Sint-niklaas", "Kortrijk",
          "Deinze", "Gent", "Lede", "Erpe-Mere", "Wetteren", "Aalst", "Aalter", "Ninove", "Opwijk"]
klinkers = ["a","e","i","o","u","y"]

#dit is een manier
#for stad in steden[:]:
#   if stad[0].lower() in klinkers:
# steden.remove(stad)

#betere manier om dit op te lossen is om de lijst van vanachter beginnen te controleren.
#zelf geschreven tijdens het voorbeeld van de for i in length...
for stad in steden[::-1]:
    if stad[0].lower() in klinkers:
        steden.remove(stad)

#hieronder wordt gebruik gemaakt van list comprehension
#maakt tijdelijk een nieuwe lijst aan op deze manier:
steden = [stad for stad in steden if stad[0].lower() not in klinkers]

print(steden)
