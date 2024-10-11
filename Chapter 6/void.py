def toto(a,b):
    r = a + b

print(toto(1, 2)) #Result is NONE because we're not printing "r", but we're printing the function that we call

lst = [1, 4, 6, 2 , 4, 8]
lst.sort() #void function - returned NONE - sorts internally and returns NONE
for l in lst:
    print(l)
