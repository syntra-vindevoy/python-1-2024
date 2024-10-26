weights = [1, 3, 9, 27]
target_weight = 40

def recursive_sum(weights, index=0):
    if index == len(weights):
        return 0
    return weights[index] + recursive_sum(weights, index + 1)


total_weight_recursive = recursive_sum(weights)
assert total_weight_recursive == target_weight