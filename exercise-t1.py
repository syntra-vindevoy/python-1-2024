import math
radius = 5
volume = (4/3) * math.pi * radius**3
print(f"The volume of a sphere with radius {radius} cm is {volume:.2f} cm³")
 ###########

import math
x = 42
sin_x = math.sin(x)
cos_x = math.cos(x)
sum_of_squares = sin_x**2 + cos_x**2
print(f"For x = {x}, (cos(x))^2 + (sin(x))^2 = {sum_of_squares:.10f}")

###########

import math
result = math.e ** 2
print(result)

############
cover_price = 24.95
discount = 0.40
num_copies = 60
first_copy_shipping_cost = 3
additional_copy_shipping_cost = 0.75

discounted_price = cover_price * (1 - discount)
total_book_cost = num_copies * discounted_price
total_shipping_cost = first_copy_shipping_cost + (num_copies - 1) * additional_copy_shipping_cost
total_wholesale_cost = total_book_cost + total_shipping_cost

print(f"The total wholesale cost for {num_copies} copies is ${total_wholesale_cost:.2f}")
###################
import datetime

start_time = datetime.datetime(2023, 1, 1, 6, 52)

easy_pace = datetime.timedelta(minutes=8, seconds=15)
tempo_pace = datetime.timedelta(minutes=7, seconds=12)

total_time = easy_pace + (tempo_pace * 3) + easy_pace

end_time = start_time + total_time

print(f"You'll get home at {end_time.strftime('%I:%M %p')}")

