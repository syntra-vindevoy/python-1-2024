unit_price = 24.95
discount = unit_price * 40/100
first_shipment = 3
later_shipment = 0.75
nbr_copies = 10000

price_with_discount = round(unit_price - discount, 2)

shipment_costs = first_shipment + ((nbr_copies - 1) * later_shipment)

total_cost = (nbr_copies * price_with_discount) + shipment_costs

print(total_cost)