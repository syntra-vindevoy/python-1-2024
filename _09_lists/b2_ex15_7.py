def has_duplicates(s) -> bool:
    t = list(s)
    t = sorted(t)
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

t = [1, 1, 2, 3, 5, 8]
print(has_duplicates(t))
