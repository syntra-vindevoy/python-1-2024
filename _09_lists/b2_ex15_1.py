def nested_sum(l:list) -> int:
    total = 0

    for e in l:
        total += sum(e)
    return total

t = [[1,2],[3], [4,5,6]]
print(nested_sum(t))