#
#
# def farmer_stone(target_weight):
#     # Convert to integer cents to handle fractional parts accurately
#     weights = [1, 3, 9, 27]
#     total_weight = 0
#
#     result = []
#
#     for weight in weights:
#         if target_weight < weight > target_weight:
#             opp_weight = weight
#             print(f"in the opposite scale, {opp_weight}kg")
#             mod = weight % target_weight
#             cal = mod + target_weight
#             print(f"in the scale with the weight, {mod}kg")
#             print(opp_weight)
#         elif target_weight > weight:
#             result.append(weight)
#             total_weight += weight
#             print(total_weight)
#             if total_weight >= target_weight:
#
#
#             # if cal == weight:
#             #     print(f"in the opposite scale, {cal}kg")
#             #     return
#             # elif cal != weight:
#             #
#             #     print(cal)
# farmer_stone(target_weight=21)
#
# def farmer_stone(target):
#     weights = [1, 3, 9, 27, 81]
#     solution = []
#
#     for weight in weights:
#         # Check the possible placement of each weight
#         if target % (weight * 3) == weight:  # Place weight on the left side
#             print(target % (weight * 3))
#             solution.append(f"Left: {weight}kg")
#             target -= weight
#         elif target % (weight * 3) == (weight * 2) % (weight * 3):  # Place weight on the right side
#             solution.append(f"Right: {weight}kg")
#             target += weight
#         else:
#             solution.append(f"Not used: {weight}kg")  # Don't use the weight
#     print(solution)
#     return solution
#
#
# # Example usage:
# target_weight = int(input("Enter the target weight (1 to 40): "))
# placements = farmer_stone(target_weight)
#
# print(f"To weigh {target_weight}kg, place the weights as follows:")
# for placement in placements:
#     print(placement)
#
import datetime

start = datetime.now()
def farmer_stone(target):
    weights = [1, 3, 9, 27, 81]
    solution = []

    for weight in weights:
        remainder = target % (weight * 3)

        if remainder == weight:  # Place weight on the left side
            solution.append(f"Left: {weight}kg")
            target -= weight
        elif remainder == (weight * 2) % (weight * 3):  # Place weight on the right side
            solution.append(f"Right: {weight}kg")
            target += weight
        else:  # Don't use the weight
            solution.append(f"Not used: {weight}kg")

    return solution


# Example usage:
target_weight = int(input("Enter the target weight (1 to 40): "))
placements = farmer_stone(target_weight)

print(f"To weigh {target_weight}kg, place the weights as follows:")
for placement in placements:
    print(placement)
end = datetime.now()

print(f"Time taken: {end - start}")

