# Verwijder uit de lijst alle steden die beginnen met een klinker. Pop of remove gebruiken.

steden = ['oudenaarde', 'zottegem', 'sint-niklaas', 'kortrijk', 'deinze', 'gent', 'wetteren', 'erpe-mere', 'aalst', 'ninove', 'aalter', 'opwijk']

klinkers = 'a', 'e', 'i', 'o', 'u'

for stad in steden[::-1]:
    print("Ik controleer", stad)
    begin = stad[0].lower()

    if begin in "aeuioy":
        print("Ik verwijder ", stad)
        steden.remove(stad)


steden = [stad for stad in steden if stad[0].lower() not in "aeiouy"]

print (steden)