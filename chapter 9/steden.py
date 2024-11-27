
#steden = ["Oudenaarde", "Zottegem", "Sint-Niklaas", "Kortrijk", "Deinze", "Gent", "Lede", "Erpe-Mere", "Wetteren", "Aalst", "Ninove", "Aalter", "Opwijk"]
#klinkers = ("A", "E", "I", "O", "U")

#steden = [stad for stad in steden if stad[0] not in klinkers]

#print(steden)

def no_klinkers():
    steden = ["Oudenaarde", "Zottegem", "Sint-Niklaas", "Kortrijk", "Deinze", "Gent", "Lede", "Erpe-Mere", "Wetteren",
              "Aalst", "Ninove", "Aalter", "opwijk"]
    klinkers = ["A", "E", "I", "O", "U"]
    for i in range (len(steden)-1, -1, -1):
        if steden[i][0].upper() in klinkers:
            steden.pop(i)
    print (steden)
no_klinkers()
