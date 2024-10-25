BILLS = [500, 200, 100, 50, 20, 10, 5]
COINS = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]



def main():
    price = 2689
    used_bills: dict[int:int] = calculate_money(price, BILLS)
    used_counts: dict[int:int] = calculate_money(used_bills[1], COINS)
    print_report("Bills",used_bills[0])
    print_report("Coins", used_counts[0])


def print_report(type_values, values: dict):
    for b in values:
        print(f"{type_values} {b} * {values[b]}")
    print()

def calculate_money(price, values:[]):
    money: dict[int:int]={}
    for v in values:
        bil = price // v
        if bil > 0:
            money[v] = int(bil)
            price = price % v
    return money, price


if __name__ == '__main__':
    main()
