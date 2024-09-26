#oefening 2_1

import math

radius = 5
volume = 4/3 * math.pi * radius ** 3
print(f"The volume with a radius of {radius} cm is {volume} cubic centimetres")

#ofening 2_2

x = 42
val_cos = math.cos(x) ** 2
val_sin = math.sin(x) ** 2
val_sum = val_cos + val_sin
print(f"the cos of {x} is {val_cos} and the sin of {x} is {val_sin}, the sum of both is {val_sum}")

#oplossing 2_2

import math

x = 5

result = math.cos(x) **2 + math.sin(x) ** 2
deviation = abs(result - 1)

if deviation < 10 ** -5:
    print("het is ok")
else:
    print(f"het is niet ok want de uitkomst is {result}")

#oefening 2_3

method1 = math.e ** 2
print(method1)
method2 = math.pow(math.e,2)
print(method2)
method3 = math.exp(2)
print(method3)

#oefening 3

base_price = 24.95
store_disc = 0.60
ship_cost_ini = 3
ship_cost_add = 0.75
amount = 60

cost_base = round(base_price * amount * store_disc, 2)
ship_cost = round(ship_cost_ini + (ship_cost_add * (amount - 1)), 2)
total_cost = round(cost_base + ship_cost, 2)

print(f"de totale cost is ${total_cost}, waar van de boeken zelf ${cost_base} en verzending ${ship_cost}")

#oefening 4

time_start = 6 * 3600 + 52 * 60
easy_pace = 8 * 60 + 15
tempo_pace = 7 * 60 + 12
easy_miles = 2
tempo_miles = 3

total_time = time_start + easy_miles * easy_pace + tempo_pace * tempo_miles
hours = total_time // 3600
minutes = (total_time - hours * 3600) // 60
seconds = total_time - hours * 3600 - minutes * 60
print(f"ik kom thuis om {hours}:{minutes} and {seconds} seconds")
