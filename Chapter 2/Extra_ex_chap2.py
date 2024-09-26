#Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
#Shipping costs $3 for the first copy and 75 cents for each additional copy.
#What is the total wholesale cost for 60 copies?

book_price = 24.95
store_price = book_price - (book_price * 0.4)
copies = 60
shipping_cost = 3 + ((copies - 1) * 0.75)
total_cost = (copies * store_price) + shipping_cost
print(f"The wholesale cost for 60 copies is ${total_cost:.2f}")

