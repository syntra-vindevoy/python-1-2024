x=42
y=42
z= x*60+y
print (x, "minutes +", y, "seconds=", z, "seconds")
x=10
y=x*1.61
print ("there are", y, "miles in", x, "kilometers" )
a=z/y
print ("the pace is", a, "seconds per mile")
b=a/60
c=a-(int(b)*60)
print ("that equals", int(b), "minutes, and", c, "seconds per mile")
print ("or", int (b), "minutes,", int(c), "seconds and", round (((a-int(a))*100)), "hundreds")
h=60*60
i=z/h
print ("the average speed is", i*y, "miles per hour")
