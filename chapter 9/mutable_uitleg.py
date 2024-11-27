#volgende in mutable
c = ["een", "twee", "drie"]
d = c
e = c.copy ()
c.append("vier")
print (d)  #d is aangespast omdat c een list was en mutable is
print (e)

#volgende is unmutable
x = 5
y = x
x = 6  #y wordt niet aangepast omdat x en y unmutable zijn
print (y)
