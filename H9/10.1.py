def nested_sum(nested_lists):
    return sum(sum(inner_list) for inner_list in nested_lists)

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
