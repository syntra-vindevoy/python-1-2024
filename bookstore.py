#2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
#$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
#60 copies?


unitprice = 24.95
shippingcost = 3

discount = 40

current_price = unitprice - ((unitprice / 100)*40)

first_copie = 3.0
other_copies = 0.75
total_copies = 60 - 1
all_copies = 60

shipment_cost = first_copie + other_copies * total_copies
total_cost = current_price * all_copies + shipment_cost
print(total_cost)



