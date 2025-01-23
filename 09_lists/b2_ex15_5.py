def is_sorted(l:list) -> bool:
    return l == sorted(l)

t = [1, 2, 3, 4, 5]
print(is_sorted(t))

t = ["b", "a", "c"]
print(is_sorted(t))