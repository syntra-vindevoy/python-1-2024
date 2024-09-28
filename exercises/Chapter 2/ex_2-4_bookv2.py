base_price = 24.95
store_disc = 0.60
ship_cost_ini = 3
ship_cost_add = 0.75
amount = 60

cost_base = round(base_price * amount * store_disc, 2)
ship_cost = round(ship_cost_ini + (ship_cost_add * (amount - 1)), 2)
total_cost = round(cost_base + ship_cost, 2)

print(f"de totale cost is ${total_cost}, waarvan de boeken zelf ${cost_base} en verzending ${ship_cost}")
