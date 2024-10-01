minutes=42
sec=42
tot_sec= minutes*60+sec
print (f"{minutes} minutes {sec} seconds= {tot_sec} seconds")
km=10
miles=km/1.61
print (f"there are {miles} miles in {km} kilometers")
pace=tot_sec/miles
print (f"the pace is {pace} seconds per mile")
pace_per_min=pace/60
pace_sec_rest=pace-(int(pace_per_min)*60)
print (f"that equals {int(pace_per_min)} minutes, and {pace_sec_rest} seconds per mile")
print (f"or {int (pace_per_min)} minutes, {int(pace_sec_rest)} seconds and {round (((pace-int(pace))*100))} hundreds")
i=tot_sec/3600 #aantal sec t.o.v. een uur
print (f"the average speed is {i*miles} miles per hour, ({round((i*miles)*100)/100})miles per hour")
