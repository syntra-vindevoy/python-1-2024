# ## coins
# def calculate_coins_greedy(amount):
#     bills = ['500', '200', '100', '50', '20', '10', '5', '2']
#
#     coins_500 = amount // 500
#     amount %= 500
#     coins_200 = amount // 200
#     amount %= 200
#     coins_100 = amount // 100
#     amount %= 100
#     coins_50 = amount // 50
#     amount %= 50
#     coins_20 = amount // 20
#     amount %= 20
#     # Coins of denomination 10
#     coins_10 = amount // 10
#     amount %= 10
#     # Coins of denomination 5
#     coins_5 = amount // 5
#     amount %= 5
#
#     coins_2 = amount // 2
#     amount %= 2
#
#
#     # If there is any remaining amount that cannot be converted to coins
#     print(f"{coins_500} bill of 500")
#     print(f"{coins_200} bill of 200")
#     print(f"{coins_100} bill of 100")
#     print(f"{coins_50} bill of 50")
#     print(f"{coins_20} bill of 20")
#     print(f"{coins_10} bill of 10")
#     print(f"{coins_5} bill of 5")
#     print(f"{coins_10} coins of 2")
#     return coins_10 + coins_5 + coins_2 + coins_50 + coins_20
#
# print(calculate_coins_greedy(45236))  # Output: 6
# print(calculate_coins_greedy(58963))  # Output: 6
# print(calculate_coins_greedy(89743))  # Raises ValueError


# def calculate_coins_greedy(amount):
#     denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
#     counts = {denomination: 0 for denomination in denominations}
#
#     for denomination in denominations:
#         counts[denomination] = amount // denomination
#         amount %= denomination
#
#     # Print the results
#     for denomination in denominations:
#         if counts[denomination] > 0:
#             if denomination >= 10:
#                 print(f"{counts[denomination]} bills of {denomination}")
#             else:
#                 print(f"{counts[denomination]} coins of {denomination}")
#
#     # Return the total number of coins/bills used (sum of all counts)
#     total_count = sum(counts.values())
#     return total_count
#
#
# # Example Usage
# print(calculate_coins_greedy(877.57))  # Expected output should show the breakdown of each denomination
# print(calculate_coins_greedy(58963))  # Expected output should show the breakdown of each denomination


def calculate_coins_greedy(amount):
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

    # Convert to integer cents to handle fractional parts accurately
    amount = round(amount * 100)
    total_count = 0

    result = []

    for denomination in denominations:
        denom_cents = int(denomination * 100)
        if amount >= denom_cents:
            count = amount // denom_cents
            amount %= denom_cents
            total_count += count
            if denomination >= 10:
                result.append(f"{count} bills of {denomination:.0f}")
            else:
                result.append(f"{count} coins of {denomination:.2f}")

    # Print the results
    print("\n".join(result))

    return total_count


# Example Usage
print(calculate_coins_greedy(877.56))  # Breakdown of each denomination
print(calculate_coins_greedy(58963))  # Breakdown of each denomination
