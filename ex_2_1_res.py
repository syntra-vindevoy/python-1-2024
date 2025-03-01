bookPrice = 24.95
discount = .60
shippingPriceRest = .75
shippingPriceFirst = 3.00
totalUnits = 60

bookDiscountAmount = bookPrice * discount * totalUnits
shipping = shippingPriceRest * 59 + shippingPriceFirst

result = bookDiscountAmount + shipping


print ('The total price for 60 books including shipping and discount is: ')
print ('Total price of the books is: ' + str (bookDiscountAmount))
print ('Total Shipping is: ' + str(shipping))
print ('The Total price is: ' + str(result))