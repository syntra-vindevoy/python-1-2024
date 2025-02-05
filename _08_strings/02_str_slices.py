fruit = "banana"
print("The string is:", fruit)
print("The result of the slice fruit[0:3] is:", fruit[0:3])
print("Omitting 0 fruit[:3] as the start of the slice gives the same result:", fruit[:3])
print("The result of the slice fruit[3:6] is:", fruit[3:6])
print("In the example above, 6 is allowed in a slice, but not as an index")
print("Omitting the end of the slice fruit[3:] results in a slice until the end:", fruit[3:])
print("If the 1st index >= the 2nd index, the result will be an empty string fruit[3:3] =", fruit[3:3])
print("Entering no indexes will give the full string fruit[:] =", fruit[:])