
steden = ["Oudenaarde", "Zottegem", "Sint-Niklaas", "Kortrijk", "Deinze", "Gent", "Lede", "Erpe-Mere", "Wetteren", "Aalst", "Ninove", "Aalter", "Opwijk"]
klinkers = ("A", "E", "I", "O", "U")

for stad in steden[::-1]:
    begin = stad[0].upper()
    if begin in klinkers:
        steden.remove(stad)

#steden = [stad for stad in steden if stad[0].upper not in klinkers] #gebruikt intern een nieuwe lijst om te vullen met wat je nodig hebt

#print(steden)

def no_klinkers():
    steden = ["Oudenaarde", "Zottegem", "Sint-Niklaas", "Kortrijk", "Deinze", "Gent", "Lede", "Erpe-Mere", "Wetteren",
              "Aalst", "Ninove", "Aalter", "opwijk"]
    klinkers = ["A", "E", "I", "O", "U"]
    for i in range (len(steden)-1, -1, -1):
        if steden[i][0].upper() in klinkers:
            steden.remove(steden[i])
    print (steden)
no_klinkers()
