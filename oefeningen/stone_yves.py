import itertools
from itertools import combinations, product
from sortedcontainers import SortedDict



def main():
    weights = SortedDict()
    stones = [1, 3, 9, 27]

    for s in stones:
        for w in list(weights.keys()):
            weights[s + w] = [w, s]
            weights[s - w] = [-w, s]

        weights[s] = [s]

    #print(weights)
    for weight, stones in weights.items():
        print(f"Weight: {weight}, Stones: {stones}")


# def main():
#     weights = SortedDict(
#                 {
#                     sum([choice[i] * (3 ** i) for i in range(4)]): choice
#                     for choice in list(product([-1, 0, 1], repeat=4))
#                     if sum([choice[i] * (3 ** i) for i in range(4)]) > 0
#                 })
#
#     print(weights)

# def main():
#     weights = SortedDict()
#     ternary = [-1, 0, 1]
#     multipliers = [1, 3, 9, 27]
#
#     choices = list(product(ternary, repeat=4))
#
#     for choice in choices:
#         weight = sum([choice[i] * multipliers[i] for i in range(4)])
#
#         if weight < 0:
#             continue
#
#         weights[weight] = choice
#
#     print(weights)
#
#
# def main():
#     weights = {}
#     stones = [1, 3, 9, 27]
#
#     for number_left in range(1, 5):
#         for stones_left in combinations(stones, number_left):
#             stones_right = list(set(stones) - set(stones_left))
#
#             for number_right in range(0, len(stones_right) + 1):
#                 for counter_weight in combinations(stones_right, number_right):
#                     weight = sum(stones_left) - sum(counter_weight)
#
#                     if weight < 0:
#                         continue
#
#                     if weight in weights:
#                         print("This option exists already.")
#                         continue
#
#                     weights[weight] = (stones_left, counter_weight)
#
#     weights = dict(sorted(weights.items(), key=lambda item: item[0]))
#
#     print(len(weights))
#     print(weights)
#
if __name__ == "__main__":
    main()