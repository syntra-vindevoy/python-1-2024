print("----------------------------------------------------")
# 1.How many seconds are there in 42 minutes 42 seconds?
print("1.How many seconds are there in 42 minutes 42 seconds?")
minutes : 60
seconds : 1
minutes = 42
seconds = 42
output = (minutes * 60 + seconds)
print(output, "seconds.")

print("----------------------------------------------------")
# 2.How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
print("2.How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.")
kilometers : 1
Miles : 1.61
kilometers = 10
Miles = 1.61

output = (kilometers / Miles)
output = round(output, 2)
print(output," miles in 10 kilometers." )

print("----------------------------------------------------")
# 3.If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
print("3.If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?")
hour : 1

output = (minutes * 60 + seconds)
output2 = (kilometers/Miles)
output3 = (output2/output)
output3= round(output3,4)
print(output3,"mph average speed in hour.")

print("----------------------------------------------------")
# 4.What is your average pace in minutes and seconds per mile?
print("4.What is your average pace in minutes and seconds per mile?")
output1= (minutes + seconds / 60)
output3 = (output2/output1)
output3= round(output3,4)
print(output3,"mph average speed in minutes and seconds per mile.")

print("-----------------------------------------------------")
print("5.What is your average speed in miles per hour?")
output1 = (minutes / 60 + seconds / 3600)
output2 = (kilometers/Miles)
output3 = (output2/output1)
output3 = round(output3,2)
print(output3,"mph average speed in hour.")


