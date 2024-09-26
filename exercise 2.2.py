n=60
price=24.95
store_price = price*60/100
shipping = 3*1 + 0.75*(n-1)
total = store_price*n + shipping
print (total)

start= (6*60+52)*60 #sec
slow= 8*60+15
fast = 7*60+12
total_run = 2*slow + 3*fast

stop= total_run + start
uur= (int(stop/3600))
rest_min= stop-uur*3600
min= (int (rest_min/60))
rest_sec= stop-uur*3600-min*60
sec= int(rest_sec)
print (f"{uur}u, {min}m, {sec}s")
