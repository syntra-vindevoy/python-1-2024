book_price = 24.95
discount = 40 / 100

shipping_cost_first = 3
shipping_cost_other = 0.75

copies = 60

total_books = copies * book_price
total_books = total_books * (1 - discount)  # take the discount

total_shipment = shipping_cost_first + (shipping_cost_other * (copies - 1))

total_price = total_books + total_shipment

print(round(total_price, 2))
