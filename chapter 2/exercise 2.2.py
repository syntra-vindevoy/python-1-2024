
books=10000
price=24.95
discount = 40/100
shipping_first = 3
shipping_add = 0.75
store_price = price*(1-discount)
shipping = shipping_first + shipping_add*(books-1)
total = store_price*books + shipping
print (total)
alt_total = (books*price)*(1-discount) + shipping #ivm afronding van de 40% korting tov grote hoeveelheden
print (alt_total)

start= (6*60+52)*60 #hour to secs
slow= 8*60+15
fast = 7*60+12
total_run = 2*slow + 2.8*fast

#eerste versie
stop= total_run + start #seconden
uur= (int(stop/3600)) #uren
rest_min= stop-uur*3600 #seconden
minutes= (int (rest_min/60)) #minuten
sec= stop-uur*3600-minutes*60 #seconden
print (f"{uur}u, {minutes}m, {sec}s")

#tweede versie met dubbele //
stop= total_run + start #seconden
uur= int(stop//3600) #uren
rest_min= stop-uur*3600 #seconden
minutes= int(rest_min//60) #minuten
sec= stop-uur*3600-minutes*60 #seconden
print (f"{uur}u, {minutes}m, {sec}s")

#derde versie met gebruik van restwaarde
stop = total_run + start #seconden
uur = stop//3600 #uren
rest_min = stop%3600 #seconden
minutes = rest_min//60 #minuten
sec = rest_min%60 #seconden
print (f"{int(uur)}u, {int(minutes)}m, {sec}s")

#vierde versie met honderdsten
stop = total_run + start #seconden
uur = stop//3600 #uren
rest_min = stop%3600 #seconden
minutes = rest_min//60 #minuten
sec = rest_min%60 #seconden
hund = round(sec*100%100)
print (f"{int(uur)}u, {int(minutes)}m, {int(sec)}s, {hund}hundreths")

#vijfde versie
import datetime

start = datetime.timedelta(hours=6, minutes=52)
slow = datetime.timedelta(minutes=8, seconds=15)
fast = datetime.timedelta(minutes=7, seconds=12)

print(start + slow * 2 + fast * 3)

