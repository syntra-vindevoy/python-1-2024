import math

x = 5

y = 10 ** -5


sum_rule = (math.cos(x))**2 + (math.sin(x))**2

if sum_rule == 1:
    print("true")
else:
    print("false")


    #oplossing om af te ronden van Yves. (er kon ook round gebruikt worden, zeker in dit geval), maar deviation is beter.

deviation = abs(sum_rule - 1)
if deviation < 10 ** -5:  #10 ** -5 10 tot de macht -5. geeft als waarde 0.000005, gemakkelijker ipv het getal te moeten typen en te gaan tellen hoeveel x 0
    print("true")
else:
    print("false")

