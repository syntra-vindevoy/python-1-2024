strings = "Hello, World!"
mylist = strings.split(",")
print(mylist)

print(",".join(mylist))

fl= 25.25
my_string = "The price is: %.2f " % fl
print(my_string)

my_string = "The price is: {0:.2f} ".format(fl)
print(my_string)

my_string = "The price is: {price:.2f} ".format(price=fl)
print(my_string)

my_string = "The price is: {0} ".format(fl)
print(my_string)

my_string = F"The price is: {fl} "
print(my_string)
