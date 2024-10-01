###Exercise 2.11.2###
# 1: 17 = n --> syntax error

# 2: x = y = 1 --> yes you can assign variables like this

# 3: ; --> has no effect on the code, however it can be used to put multiple statements on when line (not recommended)
x = 10; y = 20; z = x + y
print(z)

# 4: putting a period at the end of a statement gives a syntax error

# 5: Writing the name of a module wrong will result in an error

###Exercise 2.11.3###
import math

radius = 5                                  #radius in cm
volume = (4/3) * math.pi * (radius ** 3)    #volume in cm²
print(f"The volume of the sphere with radius {radius} is: {volume}")


x = 5
result = (math.cos(x) ** 2) + (math.sin(x) ** 2)
dev = abs(result - 1)

if dev < (10 ** -5):
    print("The statement is TRUE")
else:
    print("The statement is FALSE")

print(f"The result of cos({x})² + sin({x})² is {round(result)}")


my_result1 = math.e ** 2
my_result2 = math.pow(math.e, 2)            # why is __y: added here???
my_result3 = math.exp(2)

print(f"The result of e² with method 1 is {my_result1}")
print(f"The result of e² with method 2 is {my_result2}")
print(f"The result of e² with method 3 is {my_result3}")

############################################################################################
print("#" * 50)

price = 24.95                                           #Unit price of book
discount = 0.4                                          #Discount of 40%
book_discount = (price * (1 - discount))                #Unit price of discounted book
amount = 10000                                          #Amount of books
init_ship = 3                                           #Init shipping price
whole_ship = 0.75                                       #Additinal shipping price

total_book = book_discount * amount
shipping = init_ship + (whole_ship * (amount - 1))
total = round((total_book + shipping), 2)

print(f"The total price for the books is {total_book}, the total shipping is {shipping} and the total amount is {total}")

############################################################################################
print("#" * 50)

start_time = ((6 * 60) + 52) * 60                       #Start time is sec
easy_peace = (8 * 60) + 15                              #Easy peace is sec
tempo_peace = (7 * 60) + 12                             #Tempo peace is sec

total_easy = 2 * easy_peace
total_tempo = 3 * tempo_peace

arrival = start_time + total_easy + total_tempo
#print(arrival)

arrival_hour = arrival // 3600              #Floor convert seconds to hours
print(arrival_hour)

arrival_minute = (arrival % 3600) // 60     #Remaining seconds after converting to hour, floor divided to min
print(arrival_minute)

arrival_second = (arrival % 60)             #Remain seconds when we convert to min
print(arrival_second)

print(f"I arrive for breakfast at {arrival_hour}:{arrival_minute}:{arrival_second} am")

############################################################################################
print("#" * 50)
import datetime

start = datetime.timedelta(hours = 6, minutes = 52)
slow = datetime.timedelta(minutes = 8, seconds = 15)
fast = datetime.timedelta(minutes = 7, seconds = 12)

print(start + (2 * slow) + (3 * fast))

two_hours_later = datetime.timedelta(hours = 2)
print(datetime.datetime.now() + two_hours_later)

############################################################################################
print("#" * 50)

#Switch x & y without additional var or tuple
x = 2
y = 3

x = x + y           # x = 5
y = x - y           # y = 5 - 3 = 2
x = x - y           # x = 5 - 2 = 3


