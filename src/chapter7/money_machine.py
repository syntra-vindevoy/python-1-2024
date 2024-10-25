BILLS = [500, 200, 100, 50, 20, 10, 5]
COINS = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]



def main():
    price = 2689
    used_bills: dict[int:int] = calculate_money(price, BILLS)
    used_counts: dict[int:int] = calculate_money(used_bills[1], COINS)
    print_report("Bills",used_bills[0])
    print_report("Coins", used_counts[0])
    print()
    print("With recursive function:")
    used_bills, remaining_price = calculate_money_recursive(price, BILLS)
    used_counts, _ = calculate_money_recursive(remaining_price, COINS)
    print_report("Bills", used_bills)
    print_report("Coins", used_counts)


def print_report(type_values, values: dict):
    for v, count in values.items():
        print(f"{type_values} {v} * {count}")
    print()

def calculate_money(price, coupures:[]):
    money: dict[int:int]={}
    for v in coupures:
        bil = price // v
        if bil > 0:
            money[v] = int(bil)
            price = price % v
    return money, price


def calculate_money_recursive(amount: float, coupures: list, index: int = 0, used_coupures=None) -> tuple:
    if used_coupures is None:
        used_coupures = {}
    if index >= len(coupures):
        return used_coupures, amount
    coupure = coupures[index]
    count = amount // coupure
    if count > 0:
        used_coupures[coupure] = int(count)
        amount %= coupure
    return calculate_money_recursive(amount, coupures, index + 1, used_coupures)


if __name__ == '__main__':
    main()
