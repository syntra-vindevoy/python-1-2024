###Exercise 10.1
t = [[1, 2], [3], [4, 5, 6]]

def nested_sum(t:list[int]) -> int:
    s = 0
    for sublist in t:
        s += sum(sublist)

    return s

print(nested_sum(t))


###Exercise 10.2
t = [1, 2, 3]

def cumsum(t:list[int]) -> list[int]:
    s = 0
    for i in range(len(t)):
        s += t[i]
        t[i] = s

    return t

print(cumsum(t))





