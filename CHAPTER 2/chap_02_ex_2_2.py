import math

price_book = 24.95
number_of_copies = 60
discount = 40/100

shippingcost_first = 3 #eerste aan 3$
shippingcost_next = 0.75 #al de rest aan 0.75cent

bookdiscount = (price_book * discount)
bookafterdiscount = (price_book - bookdiscount)

price_first = bookafterdiscount+ shippingcost_first
price_rest = (bookafterdiscount + shippingcost_next) * 59
result = price_first + price_rest
print(result)

print(round(result, 2))




