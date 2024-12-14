distancekm = 10
distancemiles = distancekm/1.61
minutes = 42
seconds = 42
timeinminutes = minutes + (seconds/60)
timeinseconds = (minutes*60) + seconds

averagespeedinmin = (distancemiles/timeinminutes)
averagespeedinsec = (distancemiles/timeinseconds)

print(averagespeedinsec)
print(averagespeedinmin)
print(averagespeedinmin*60)


