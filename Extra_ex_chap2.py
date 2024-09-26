book_price = 24.95
store_price = book_price - (book_price * 0.4)
copies = 60
shipping_cost = 3 + ((copies - 1) * 0.75)
total_cost = (copies * store_price) + shipping_cost
print(f"The wholesale cost for 60 copies is {total_cost:.2f}")

